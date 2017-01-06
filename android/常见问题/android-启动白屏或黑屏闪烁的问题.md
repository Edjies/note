完整代码： (styles 和 styles(V21))
```xml
    <style name="AppTheme.NoActionBar">
        <item name="windowActionBar">false</item>
        <item name="windowNoTitle">true</item>
        <item name="android:windowDrawsSystemBarBackgrounds">true</item>
        <item name="android:statusBarColor">@android:color/transparent</item>
    </style>

    <!--去除启动时的白屏或黑屏闪烁问题-->
    <style name="SplashTheme" parent="AppTheme.NoActionBar">
        <item name="android:windowIsTranslucent">true</item> <!-- 设置透明 -->   切换时的透明效果
    </style>
```