package com.hubble.notificaiton.progressbar;

import android.app.IntentService;
import android.app.NotificationManager;
import android.content.Intent;
import android.content.Context;
import android.os.StrictMode;
import android.support.v7.app.NotificationCompat;

import java.util.ArrayList;

/**
 * An {@link IntentService} subclass for handling asynchronous task requests in
 * a service on a separate handler thread.
 * <p/>
 * helper methods.
 */
public class MyIntentService extends IntentService {

    private static final String  ACTION_UPLOAD = "com.hubble.notificaiton.progressbar.action.upload";

    private static final String EXTRA_IMG = "img";

    private NotificationManager mNotifyManager;
    private NotificationCompat.Builder mBuilder;
    int id = 1;

    public MyIntentService() {
        super("MyIntentService");

    }

    @Override
    public void onCreate() {
        super.onCreate();
        mNotifyManager = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
        mBuilder = new NotificationCompat.Builder(this);
        mBuilder.setContentTitle("upload")
                .setContentText("upload in progress")
                .setSmallIcon(R.mipmap.ic_launcher);
    }

    /**
     * 图片上传
     */
    public static void startActionUpload(Context context, ArrayList<String> imgs) {
        Intent intent = new Intent(context, MyIntentService.class);
        intent.setAction(ACTION_UPLOAD);
        intent.putExtra(EXTRA_IMG, imgs);
        context.startService(intent);
    }

    @Override
    protected void onHandleIntent(Intent intent) {
        if (intent != null) {
            final String action = intent.getAction();
            if (ACTION_UPLOAD.equals(action)) {
                final ArrayList<String> imgUrl = intent.getStringArrayListExtra(EXTRA_IMG);
                for(int i = 0; i < imgUrl.size(); i++) {
                    handleUpload(imgUrl.get(i), i, imgUrl.size());
                }

                handleCommit(new ArrayList<String>());

            }
        }
    }

    /**
     * 上传图片
     */
    private void handleUpload(String url, int progress, int max) {
        try{
            Thread.sleep(2 * 1000);
        }catch (Exception e){
        }
        mBuilder.setProgress(max, progress, false);
        mNotifyManager.notify(id, mBuilder.build());
    }


    /**
     *  提交
     * @param urls
     */
    private void handleCommit(ArrayList<String> urls) {
        mBuilder.setProgress(0, 0, false);
        mBuilder.setContentText("上传成功");
        mNotifyManager.notify(id, mBuilder.build());
    }
}
