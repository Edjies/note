### 通过adb shell 调试android sqlite数据库

* `#创建android 模拟器`
* `> adb -s emulator-xxxx shell				#进入shell命令`
* `$ su                         			#获取root权限`
* `$ cd /data/data/<package>/databases		#进入数据库目录`	
* `$ ls                                     #查看数据库列表`
* `$ sqlite3 <your-db-name>.db              #进入数据库操作`  


### 数据库操作
* 统计查询
* select p.*,(select count(1) from PROJECT_ITEM pi where p._ID == pi.PROJECT_ID) as size from PROJECT p;


                              