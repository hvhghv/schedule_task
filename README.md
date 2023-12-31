这是我首次在github发布程序，应该不会踩到什么坑了吧哈哈~~~

# schedule_task

## 简述

* 能够延迟一定时间，每间隔一段时间，或在指定时间执行命令的脚本  

* 可用于开机后自动执行一些shell命令

* 基于python的第三方库schedule

## 注意

* 日志文件位于logging/logging.txt，只会保存上一次运行的状况。每次运行程序，该日志文件会清空。  

* 建议命令为非阻塞，或只会阻塞短暂时间。本脚本只能同时运行2种阻塞式命令。可以在源码中更改进程数来增加。

## 使用方式：   

### 1. 编写task.json



这是一个简单的task.json示例
~~~
{
    "test1":{           // test1为一项计划的名字，任意字符串
        "check":2,      // check值为2，只执行一次
        "command":"echo \"这是5秒后开始执行\"",  // 命令的内容
        "hour":0,       // 当check为2时，hour,min,sec指在脚本运行0小时0分钟5秒后执行一次
        "min":0,
        "name":"test1", //计划的名字，要与键值相同
        "path":"/",     //命令运行时的工作路径
        "sec":5
    },
    "test2":{           // test2为一项计划的名字，任意字符串
        "check":0,      // check值为0，每间隔一定时间执行
        "command":"echo \"这是每隔10秒执行\"",  // 命令的内容
        "hour":0,       // 当check为0时，hour,min,sec指在脚本运行后每间隔0小时0分钟10秒执行一次
        "min":0,
        "name":"test2", //计划的名字，要与键值相同
        "path":"/",     //命令运行时的工作路径
        "sec":10
    },
    "test3":{           // test3为一项计划的名字，任意字符串
        "check":1,      // check值为1，在每天指定时间执行
        "command":"echo \"这是在每天13:04:23执行\"", // 命令的内容
        "hour":13,      // 当check为1时，hour,min,sec指在每天的13:04:23执行一次
        "min":4,
        "name":"test3", //计划的名字，要与键值相同
        "path":"/",     //命令运行时的工作路径
        "sec":23
    }
}
~~~

强烈建议在windows系统下，使用tool/配置任务脚本.exe来编写task.json。

<img src='img/1.png'>

* 名字为name   
* 命令为command
* 间隔时间，check值为0;开始执行，check值为2;指定时间，check值为1
* 时，分，秒为hour,min,sec

*（注意，以上各项为必填项，缺少任意一项均会出现bug）*

* 添加，添加或修改一项计划  
* 删除，删除一项计划
* 加载，加载已存在的task.json文件
* 保存，保存编写好的task.json文件


### 2. 测试

* 若有python环境，可参考下列方式(此处编写好的task.json路径为"/home/task.json")

~~~
pip3 install schedule   

wget https://raw.githubusercontent.com/hvhghv/schedule_task/master/src/schedule_task.py

mkdir logging

mkdir task

cp /home/task.json task/task.json

python3 schedule_task.py

~~~

* 若无python环境，可下载win/linux文件夹,进入文件夹，将编写好的task.json替换task/task.json,运行schedule_task.exe/schedule_task.bin


### 3. 自启命令

若测试良好，即可添加自启命令

* 在windows上，可通过添加任务计划的方式

* 在linux上，可编写etc/rc.loacl并添加自启服务方式