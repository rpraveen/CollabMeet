/*
 * Copyright (C) 2012 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.collabmeet.mobile;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;

/**
 * The main activity of the API library demo gallery.
 * <p>
 * The main layout lists the demonstrated features, with buttons to launch them.
 */
public final class MainActivity extends Activity {
	private CollabMeetApplication app = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        app = (CollabMeetApplication)this.getApplication();

        Button joinButton = (Button)findViewById(R.id.join);
		joinButton.setOnClickListener(new OnClickListener() {
			@Override
			public void onClick(View v) {
				TextView userName = (TextView)findViewById(R.id.username);
				app.userName = userName.getText().toString();
				TextView password = (TextView)findViewById(R.id.password);
				app.password = password.getText().toString();
				TextView mid = (TextView)findViewById(R.id.meetingid);
				app.meetingID = mid.getText().toString();
				
				startActivity(new Intent(MainActivity.this, LocationActivity.class));
			}
		});
    }
}
