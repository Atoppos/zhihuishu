# 智慧树刷课程序

---

智慧树刷课程序，可直接运行，使用Python中的selenium库，程序已打包为.exe文件，功能如下:
1. 正常倍速
2. 自动静音
3. 自动关闭弹窗测验
4. 自动播放下一个视频
5. 自动1.5倍速
5. 播放时长达到25分钟后结束刷课(因为习惯分需要连续学习一定天数且每天只记录25分钟的学习时长，如需一次性看完所有视频，可以在结束刷课以后重新运行程序，即可持续刷课)
6. 无需打开浏览器

## 需要工具

---

谷歌浏览器、ChromeDriver (**需与浏览器版本匹配**)

ChromeDriver 下载地址:[http://chromedriver.storage.googleapis.com/index.html]

## 使用步骤

---

1. 运行exe文件，弹出控制台窗口
2. 按提示选择
3. 扫描二维码登录
4. 选择课程
5. 开始刷课

## 注意⚠️

---

- 需要将ChromeDriver与exe文件放在同一目录下
- 首次使用，需将控制台字体改为MS Gothic，以解决二维码图片加载问题，具体方法:
    - 在控制台上方边框处右键点击->选择属性->选择字体
- 在开始新课程时，智慧树会弹出签署在线学习承诺书，需要进入浏览器手动签署
- 运行时会提示是否清理进程，是因为如果在程序运行时关闭窗口，程序并没有结束，会在后台继续运行，选择清理进程会**强制杀掉所有的chrome和chromedriver进程**
- 程序在运行过程中如果出现错误或崩溃，是因为智慧树弹出了验证(偶尔会弹)，此时从浏览器进入智慧树刷课页面通过验证，重新运行程序即可

## License

---

MIT

