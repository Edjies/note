package com.huble.floatwidget;

import android.content.Context;
import android.graphics.PixelFormat;
import android.os.Build;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.view.WindowManager;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        findViewById(R.id.bt_add).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                final WindowManager mWindowManager = (WindowManager) getApplication().getSystemService(Context.WINDOW_SERVICE);
                WindowManager.LayoutParams mLayoutParams = new WindowManager.LayoutParams();
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
                    mLayoutParams.type = WindowManager.LayoutParams.TYPE_TOAST;
                } else {
                    mLayoutParams.type = WindowManager.LayoutParams.TYPE_PHONE;
                }
                mLayoutParams.flags = WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE | WindowManager.LayoutParams.FLAG_LAYOUT_NO_LIMITS | WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL;
                mLayoutParams.format = PixelFormat.RGBA_8888;
                mLayoutParams.gravity =  Gravity.RIGHT | Gravity.CENTER_VERTICAL;;
                mLayoutParams.width = WindowManager.LayoutParams.WRAP_CONTENT;
                mLayoutParams.height = WindowManager.LayoutParams.WRAP_CONTENT;
                View view = getLayoutInflater().inflate(R.layout.view_test, null);
                view.findViewById(R.id.bt_show).setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {

                    }
                });
                mWindowManager.addView(view ,mLayoutParams);
            }
        });
    }
}
