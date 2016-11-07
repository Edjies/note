package com.hubble.notificaiton.progressbar;

import android.app.IntentService;
import android.app.NotificationManager;
import android.content.Intent;
import android.content.Context;
import android.os.StrictMode;
import android.support.v7.app.NotificationCompat;

/**
 * An {@link IntentService} subclass for handling asynchronous task requests in
 * a service on a separate handler thread.
 * <p/>
 * helper methods.
 */
public class MyIntentService extends IntentService {

    private static final String  ACTION_UPLOAD = "com.hubble.notificaiton.progressbar.action.upload";

    private static final String EXTRA_IMG = "img";
    private static final String EXTRA_PROGRESS = "progress";
    private static final String EXTRA_MAX = "max";

    private NotificationManager mNotifyManager;
    private NotificationCompat.Builder mBuilder;
    int id = 1;

    public MyIntentService() {
        super("MyIntentService");

    }

    /**
     * 图片上传
     */
    public static void startActionUpload(Context context, int progress, int max) {
        Intent intent = new Intent(context, MyIntentService.class);
        intent.setAction(ACTION_UPLOAD);
        intent.putExtra(EXTRA_PROGRESS, progress);
        intent.putExtra(EXTRA_MAX, max);
        context.startService(intent);

    }

    @Override
    protected void onHandleIntent(Intent intent) {
        if (intent != null) {
            final String action = intent.getAction();
            if (ACTION_UPLOAD.equals(action)) {
                final String imgUrl = intent.getStringExtra(EXTRA_IMG);
                final int progress = intent.getIntExtra(EXTRA_PROGRESS, 0);
                final int max = intent.getIntExtra(EXTRA_MAX, 100);
                handleUpload(imgUrl, progress, max);
            }
        }
    }

    /**
     * Handle action Foo in the provided background thread with the provided
     * parameters.
     */
    private void handleUpload(String uri, int progress, int max) {
        if(mNotifyManager == null) {
            mNotifyManager = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
            mBuilder = new NotificationCompat.Builder(this);
            mBuilder.setContentTitle("upload")
                    .setContentText("upload in progress")
                    .setSmallIcon(R.mipmap.ic_launcher);
        }

        try{
            Thread.sleep(2 * 1000);
        }catch (Exception e){

        }
        mBuilder.setProgress(max, progress, false);
        mNotifyManager.notify(id, mBuilder.build());

    }
}
