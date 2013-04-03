package com.collabmeet.mobile;

import android.content.Context;
import android.location.Location;

import com.google.android.gms.maps.GoogleMap.OnMapLongClickListener;
import com.google.android.gms.maps.LocationSource;
import com.google.android.gms.maps.model.LatLng;

/**
 * A {@link LocationSource} which reports a new location whenever a user long presses the map at
 * the point at which a user long pressed the map.
 */
public class MobileLocationSource implements LocationSource, OnMapLongClickListener {
	private OnLocationChangedListener mListener;

	/**
	 * Flag to keep track of the activity's lifecycle. This is not strictly necessary in this
	 * case because onMapLongPress events don't occur while the activity containing the map is
	 * paused but is included to demonstrate best practices (e.g., if a background service were
	 * to be used).
	 */
	private boolean mPaused;
	private Context mContext = null;
	private GPSTracker mGPS = null;

	public MobileLocationSource(Context context) {
		mContext = context;
		mGPS = new GPSTracker(mContext, this);
	}

	@Override
	public void activate(OnLocationChangedListener listener) {
		mListener = listener;
	}

	@Override
	public void deactivate() {
		mListener = null;
	}

	@Override
	public void onMapLongClick(LatLng point) {
		if (mListener != null && !mPaused) {
			Location location = new Location("LongPress");
			location.setLatitude(point.latitude);
			location.setLongitude(point.longitude);
			location.setAccuracy(50);
			updateLocation(location);
		}
	}

	public void updateLocation(Location uLocation) {
		if (mListener != null && !mPaused) {
			/* Update local map */
			Location location = new Location(uLocation.getProvider());
			location.setLatitude(uLocation.getLatitude());
			location.setLongitude(uLocation.getLongitude());
			location.setAccuracy(uLocation.getAccuracy());
			mListener.onLocationChanged(location);
			
			/* Broadcast location */
			((LocationActivity)mContext).app.broadcastLocation(location);
			
			/* Update display */
			((LocationActivity)mContext).setMapText();
		}
	}

	public void onPause() {
		mPaused = true;
	}

	public void onResume() {
		mPaused = false;
	}

}
