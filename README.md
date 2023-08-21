# schedule_task

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
        "path":"/",
        "sec":10
    },
    "test3":{           // test3为一项计划的名字，任意字符串
        "check":1,      // check值为1，在每天指定时间执行
        "command":"echo \"这是在每天13:04:23执行\"", // 命令的内容
        "hour":13,      // 当check为1时，hour,min,sec指在每天的13:04:23执行一次
        "min":4,
        "name":"test3", //计划的名字，要与键值相同
        "path":"/",
        "sec":23
    }
}
~~~

强烈建议在windows系统下，使用tool/配置任务脚本.exe来编写task.json。

<img src='img/1.png'>

* 名字为name   
* 命令为command
* 间隔时间，check值为0，开始执行，check值为2，指定时间，check值为1
* 时，分，秒为hour,min,sec
* 添加，添加一项计划
* 删除，删除一项计划
* 加载，加载已存在的task.json文件
* 保存，保存编写好的task.json文件


### 2. 添加自启

* 在windows上，可通过添加任务计划的方式

* 在linux上，可编写etc/rc.loacl并添加自启服务方式

### 3. 自启命令

