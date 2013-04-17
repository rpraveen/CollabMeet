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

import android.location.Location;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;
import android.widget.TextView;

import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.SupportMapFragment;

/**
 * This shows how to use a custom location source.
 */
public class LocationActivity extends FragmentActivity {

	private MobileLocationSource mLocationSource;
	public CollabMeetApplication app = null;

	private GoogleMap mMap;
	private TextView mText;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.basic_demo);

		app = (CollabMeetApplication)this.getApplication();
		mText = (TextView)LayoutInflater.from(getBaseContext()).inflate(R.layout.textview, null);
		ViewGroup textContainer = (ViewGroup) findViewById(R.id.textContainer);
		textContainer.addView(mText);

		mLocationSource = new MobileLocationSource(this);

		setUpMapIfNeeded();
		
		ServerAPI server = new ServerAPI(this);
		server.sendGET("/config.txt");
	}

	@Override
	protected void onResume() {
		super.onResume();
		setUpMapIfNeeded();

		mLocationSource.onResume();
	}

	private void setUpMapIfNeeded() {
		// Do a null check to confirm that we have not already instantiated the map.
		if (mMap == null) {
			// Try to obtain the map from the SupportMapFragment.
			mMap = ((SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map))
					.getMap();
			// Check if we were successful in obtaining the map.
			if (mMap != null) {
				setUpMap();
			}
		}
	}

	private void setUpMap() {
		mMap.setLocationSource(mLocationSource);
		mMap.setOnMapLongClickListener(mLocationSource);
		mMap.setMyLocationEnabled(true);

		setMapText();
	}

	public void setMapText() {
		if(mText != null) {
			String str = "Username = " + app.userName + "\nMeeting ID = " + app.meetingID;
			str += "\nMembers = " + app.members;
			
			Location l = mMap.getMyLocation();
			if(l != null) {
				str += "\nLatitude = " + l.getLatitude() + "\nLongitude = " + l.getLongitude() + "\nAccuracy = " + l.getAccuracy() + " metres";
			}
			
			str += "\nLocation update Count = " + app.locUpdateCount;
			
			if(app.status.length() > 0) {
				str += "\nStatus = " + app.status;
			}
			
			mText.setText(str);
		}
	}
	
	public void processServerResults(String res) {
		if(res.endsWith("\n")) {
			res = res.substring(0, res.length() - 1);
		}
		
		app.members = res;
		app.broadcastLocation(mMap.getMyLocation());
		
		setMapText();
	}

	@Override
	protected void onPause() {
		super.onPause();
		mLocationSource.onPause();
	}

	public void setDebugLogsEnabled(View v) {
		if(((CheckBox) v).isChecked()) {
			if(mText == null) {
				mText = (TextView) LayoutInflater.from(getBaseContext()).inflate(R.layout.textview, null);
				ViewGroup textContainer = (ViewGroup) findViewById(R.id.textContainer);
				textContainer.addView(mText);
				setMapText();
			}
		}
		else if (mText != null) {
			ViewGroup textContainer = (ViewGroup) findViewById(R.id.textContainer);
			textContainer.removeView(mText);
			mText = null;
		}
	}
	
	public void setBroadcastLocationEnabled(View v) {
		if(((CheckBox) v).isChecked()) {
			app.isBroadcastEnabled = true;
			app.broadcastLocation(mMap.getMyLocation());
			setMapText();
		}
		else {
			app.isBroadcastEnabled = false;
		}
	}
}
