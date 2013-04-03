package com.collabmeet.mobile;

import android.app.Application;

public class CollabMeetApplication extends Application {
	public String userName = "";
	public String password = "";
	public String meetingID = "";
	public String members = "";
	public int locUpdateCount = 0;
	
	@Override
	public void onCreate() {
		super.onCreate();
	}
}
