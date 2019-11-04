# AutoWanXue

## 使用方法

### 第一步，设置cookie

登录后复制一份学习页面的cookie。

![Kzaf29.png](https://s2.ax1x.com/2019/11/04/Kzaf29.png)

之后在项目的根目录放一个文件名为**cookie**的文件，里面存入你复制的cookie。

![KzdWo8.jpg](https://s2.ax1x.com/2019/11/04/KzdWo8.jpg)

### 第二步，运行脚本

在这之前，你得保证当前系统已经正确的安装了Python3.x环境，详情可以上网找找教程

打开控制台，运行`python DoCourse.py`即可开始刷课。

## 文件排布

| FileName   | Usage                        |
|------------|------------------------------|
| GenJSON.py | 手动生成格式化的JSON答案存档 |

## 网络请求

### 完成课程请求

<https://jluzh.wanxue.cn/sls/jwExam/addRecord>

POST

```text
data	finish_21037=A&finish_21038=A&finish_21039=A&finish_21040=B&finish_21041=B&finish_21042=B&finish_21042=C&finish_21043=A&finish_21043=B&finish_21044=B&finish_21044=D&finish_21045=D&finish_21046=D&courseId=1012&startTime=1572679274430&em=2_7023
startTime	1572679274430
courseId	1012
em	2_7023
```

### 答案请求

<https://jluzh.wanxue.cn/sls/jwExam/examAnalysis?em=2_6977&courseId=1012>

GET

```TEXT
em 2_6977

courseId 1012
```

#### 第一课

| data        | startTime      | courseId | em     |
|-------------|----------------|----------|--------|
| 20637-20646 | unix tumestamp | 1012     | 2_6977 |

#### 第二课

| data        | startTime      | courseId | em     |
|-------------|----------------|----------|--------|
| 20647-20656 | unix tumestamp | 1012     | 2_6978 |

#### 最后一课

| data        | startTime      | courseId | em     |
|-------------|----------------|----------|--------|
| 21037-21046 | unix tumestamp | 1012     | 2_7023 |


## 课程表

```text
第一单元 紧密协同团队 2-3

6977-6978

第二单元 核心通用能力 5-25

6980-7000

第三单元 企业职务能力 26-40

7002-7015

第四单元 职业发展领域选择 42-43

7017-7018

第五单元 高层次人脉网络构建 45-48

7020-7023
```

| Units  | Class Num | Id Range  |
|--------|-----------|-----------|
| Unit 1 | 2-3       | 6977-6978 |
| Unit 2 | 5-25      | 6981-7000 |
| Unit 3 | 26-40     | 7002-7015 |
| Unit 4 | 42-43     | 7017-7018 |
| Unit 5 | 45-48     | 7020-7023 |
