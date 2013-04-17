package com.collabmeet.mobile;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

import android.app.Application;
import android.location.Location;
import android.os.AsyncTask;

public class CollabMeetApplication extends Application {
	public String userName = "";
	public String password = "";
	public String meetingID = "";
	public String members = "";
	public String status = "";
	public int locUpdateCount = 0;
	public final int UDP_RECEIVE_PORT = 5005;
	public boolean isBroadcastEnabled = true;

	@Override
	public void onCreate() {
		super.onCreate();
	}

	public void broadcastLocation(Location loc) {
		if(!isBroadcastEnabled || members.length() == 0 || loc == null) {
			return;
		}
		
		String msg = userName + "," + locUpdateCount + "," + loc.getLatitude() + "," + loc.getLongitude();
		locUpdateCount++;
		
		new BroadcastInBackground().execute(msg, members);
	}
	
	private class BroadcastInBackground extends AsyncTask<String, Void, Boolean> {

		@Override
		protected Boolean doInBackground(String... params) {
			String msg = params[0];
			String ipAddresses = params[1];
			
			try {
				/* Create new UDP-Socket */
				DatagramSocket socket = new DatagramSocket();

				/* Prepare some data to be sent. */			
				byte[] buf = msg.getBytes();
				

				for (String ip: ipAddresses.split(",")) {
					System.out.println("Sending location to " + ip);
					
					/* Retrieve the ServerName */
					InetAddress serverAddr = InetAddress.getByName(ip);

					/* Create UDP-packet with data & destination (url+port) */
					DatagramPacket packet = new DatagramPacket(buf, buf.length, serverAddr, UDP_RECEIVE_PORT);

					/* Send out the packet */
					socket.send(packet);
				}
			} catch (Exception e) {
				status = "UDP transmit error!";
				e.printStackTrace();
				return false;
			}
			
			return true;
		}

		protected void onPostExecute(Boolean flag) {
			System.out.println("UDP transmit result: " + flag);
		}
	}
}