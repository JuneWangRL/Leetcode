# Hadoop-Hive-Spark 伪分布式安装

## 创建hduser用户和hadoop用户组
```sh
sudo useradd -m hduser -s /bin/bash    
sudo passwd hduser                     # 设置密码
sudo adduser hduser sudo
sudo addgroup hadoop
sudo adduser hduser hadoop
```


## 安装Hadoop

### 解压安装
在`/opt/`目录下准备hadoop的tar.gz源码解压hadoop
```sh
sudo tar -zxf ./hadoop-2.7.3.tar.gz    # 解压到/usr/local中
sudo mv ./hadoop-2.7.3/ ./hadoop       # 将文件夹名改为hadoop
```
### 并配置权限给用hduser账户

```sh
sudo chown -R hduser ./hadoop          # 开放权限给hduser
sudo chgrp -R hadoop ./hadoop          # 开放权限给hadoop分组
```

### 测试Hadoop使用权限

```sh
# 在`/opt/hadoop`目录下
 ./bin/hadoop version
```

### 使用自带例子检查Hadoop运行
```sh
mkdir ./input
cp ./etc/hadoop/*.xml ./input   # 将配置文件作为输入文件
./bin/hadoop jar ./share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar grep ./input ./output 'dfs[a-z.]+'
cat ./output/*                  # 检查运行结果
```


## 伪分布式配置

### 修改配置文件
在`hadoop/etc/hadoop/`路径中，伪分布式需要修改2个配置文件 core-site.xml 和 hdfs-site.xml
#### 修改core-site.xml
```xml
  <configuration>
    <property>
       <name>hadoop.tmp.dir</name>
       <value>file:/usr/local/hadoop/tmp</value>
       <description>Abase for other temporary directories.</description>
    </property>
    <property>
       <name>fs.defaultFS</name>
       <value>hdfs://localhost:9000</value>
    </property>
  </configuration>
```
#### 修改hdfs-site.xml
```xml
  <configuration>
    <property>
       <name>dfs.replication</name>
       <value>1</value>
    </property>
    <property>
       <name>dfs.namenode.name.dir</name>
       <value>file:/usr/local/hadoop/tmp/dfs/name</value>
    </property>
    <property>
       <name>dfs.datanode.data.dir</name>
       <value>file:/usr/local/hadoop/tmp/dfs/data</value>
    </property>
</configuration>
```
#### 格式化Namenode
后续操作全在`hadoop/`目录下
```sh
./bin/hdfs namenode -format # 确认successfully formatted
```
#### 针对localhost添加JAVA_HOME路径
```sh
# 修改./etc/hadoop/hadoop-env.sh中设JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
```
#### 添加hadoop环境于`~/.bashrc`
```sh
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
```
#### 启动Hadoop
```sh
./sbin/start-dfs.sh
```
#### `jps`检查进程
```
# 成功启动则会列出如下进程: “NameNode”、”DataNode” 和 “SecondaryNameNode”
jps
```


#### 访问 Web 界面
访问http://localhost:50070 



## 安装MySQL作为元数据库

### `apt-get`安装

```sh
sudo -E apt-get install mysql-server 
```

### MySQL基本操作

```sh
# 启停
service mysql start
service mysql stop 
# 登录
mysql –u root –p 
```

###  增加hive用户、建库、授权
```mysql
create user 'hive' identified by 'hive';
update mysql.user set authentication_string=PASSWORD("hive") where user="hive"; 
create database hive;
grant all privileges on hive.* to hive;
```



## 安装Hive

### 解压并更改权限

```sh
# 在/opt/目录下准备呀tar.gz文件
sudo tar -zxf apache-hive-2.1.1-bin.tar.gz
mv ./apache-hive-2.1.1-bin/ ./hive
# 更改权限
sudo chown -R hduser ./hive
sudo chgrp -R hadoop ./hive 
```

### 添加环境变量

#### `vim /etc/profile`

```sh
# 末尾添加
export HIVE_HOME=/usr/local/hadoop/hive
export PATH=$PATH:$HIVE_HOME/bin
```

### 修改Hive配置

#### 复制配置模板

```sh
cd hive/conf/
cp hive-default.xml.template hive-site.xml 

```

#### 修改hive-env.sh（新增的一步）

```sh
cp hive-env.sh.template hive-env.sh
sudo vim hive-env.sh
HADOOP_HOME=/apps/hadoop
export HIVE_CONF_DIR=/apps/hive/conf
```



#### `vim hive-site.xml`增加配置

```xml
  <property>
    <name>javax.jdo.option.ConnectionURL</name>
    <value>jdbc:mysql://localhost:3306/hive?createDatabaseIfNotExist=true</value>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionDriverName</name>
    <value>com.mysql.jdbc.Driver</value>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionUserName</name>
    <value>hive</value>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionPassword</name>
    <value>hive</value>
  </property>
  <property>  
    <name>hive.metastore.schema.verification</name>  
    <value>false</value>  
  </property>
  <property>
    <name>hive.metastore.warehouse.dir</name>
    <value>/usr/local/hadoop/hive/warehouse</value>
    <description>location of default database for the warehouse</description>
  </property>

  <!-- 新增的配置 -->
  <property>
  	<name>hive.querylog.location</name>
  	<value>/apps/hive/iotmp/querylog</value>
  	<description>Location of Hive run time structured log file</description>
  </property>
  <property>
  	<name>hive.server2.logging.operation.log.location</name>
  	<value>/apps/hive/iotmp/operation_logs</value>
  	<description>Top level directory where operation logs are stored if logging functionality is enabled</description>
  </property>
  <property>
  	<name>hive.server2.logging.operation.log.location</name>
  	<value>/apps/hive/iotmp/operation_logs</value>
  	<description>Top level directory where operation logs are stored if logging functionality is enabled</description>
  </property>
  <property>
  	<name>hive.downloaded.resources.dir</name>
  	<value>/apps/hive/iotmp/resource_dir</value>
  	<description>Temporary local directory for added resources in the remote file system.</description>
  </property>
  <property>
  	<name>hive.exec.local.scratchdir</name>
  	<value>/apps/hive/iotmp/scratchdir</value>
  	<description>Local scratch space for Hive jobs</description>
  </property>
```

#### 修改IO临时文件夹配置 (上面新增了配置，跳过了这一步)

- 建立IO临时文件夹 `mkdir /home/hduser/hiveiotmp`
- 查看hive-site.xml配置将所有`${system:java.io.tmpdir}`替换为`/home/hduser/hiveiotmp`
- `hive.exec.local.scratchdir` 的`${system：user.name} `改为`${user.name}`

### 增加MySQL连接

将mysql-connector-java-5.1.41.tar.gz文件中的mysql-connector-java-5.1.41-bin.jar放入/hive/lib目录下，然后执行初始化

```sh
./schematool -initSchema -dbType mysql
```

###启动并测试Hive

```sh
hive
```



## 安装Spark

### 在`/opt/`路径下解压tgz源码、改名、改权限
```sh
sudo tar -xzvf spark-2.1.0-bin-hadoop2.7.tgz
sudo mv spark-2.1.0-bin-hadoop2.7 spark
sudo chown -R hduser spark
sudo chgrp -R hadoop spark
```
### 准备环境文件
```sh
cp conf/spark-env.sh.template conf/spark-env.sh
vim conf/spark-env.sh
```
### 添加环境变量
```sh
# 需要先安装好scala
# 可先通过locate share/scala获取scala路径
export SCALA_HOME=/usr/share/scala-2.11
export SPARK_WORKER_MEMORY=1g  
```
### 准备slave文件
```sh
# 伪分布式配置文件只需要有localhost
cp conf/slaves.template conf/slaves
```
### 增加对spark-shell的软连接
```sh
sudo ln -s /bin/spark-shell /sbin
ln -s /bin/spark-shell /bin
```
### 配置Spark连接Hive/Hadoop
#### 复制Hive配置项
```sh
cp /opt/hive/conf/hive-site.xml /opt/spark/conf/
```
#### 复制Hadoop配置项
```sh
cp /opt/hadoop/etc/hadoop/core-site.xml /opt/spark/conf/
cp /opt/hadoop/etc/hadoop/hdfs-site.xml /opt/spark/conf/
```
### 添加MySQL连接器
```sh
cp /opt/hive/lib/mysql-connector-java-5.1.41-bin.jar /opt/spark/jars/
```
### 启动并测试Spark-shell
#### 启动
```sh
spark-shell
```
#### 测试
```scala
import org.apache.spark.sql.SQLContext
val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)
val df = sqlContext.sql("SHOW DATABASES")
df.show
```

### 启动并测试PySpark

#### 启动

```
pyspark
```

#### 测试

```python
rdd = sc.parallelize([(0,1), (0,1), (0,2), (1,2)])
df = sqlContext.createDataFrame(rdd, ["id", "score"])
df.show()
```

### 多用户

**Ubuntu新建用户，正常使用hadoop、hive、spark**

```shell
sudo useradd -m hiveuser -s /bin/bash
sudo passwd hiveuser
sudo adduser hiveuser sudo
sudo adduser hiveuser hadoop
```

**原因：同组的其他用户只有读、执行权，没有写入权**

```shell
# 修改权限
# 775：同组用户都拥有读、写和执行权
sudo chmod 775 /apps/hadoop -R
sudo chmod 775 /apps/hive -R
sudo chmod 775 /apps/spark -R
```

**添加环境变量（所有用户可用）**

```sh
sudo vim /etc/profile

export HADOOP_HOME=/apps/hadoop
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/bin

export HIVE_HOME=/apps/hive
export PATH=$PATH:$HIVE_HOME/bin

export SPARK_HOME=/apps/spark
export PATH=$PATH:$SPARK_HOME/bin

# 每个用户都需运行一遍下面命令
source /etc/profile
```



