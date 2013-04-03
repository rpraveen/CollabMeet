package com.collabmeet.mobile;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.protocol.BasicHttpContext;
import org.apache.http.protocol.HttpContext;

import android.os.AsyncTask;


public class ServerAPI {
	//private static String serverURL = "whatscookingserver.herokuapp.com";
	public static String serverURL = "192.168.0.104:1337";
	private String uri;
	private List<NameValuePair> nameValuePairs;
	private LocationActivity locListener = null;

	public ServerAPI(LocationActivity locListener) {
		super();
		this.locListener = locListener;
	}

	public void sendGET(String uri) {
		this.uri = uri;
		
		new LongRunningGetIO().execute();
	}
	
	public void sendPOST(String uri, List<NameValuePair> nameValuePairs) {
		this.uri = uri;
		this.nameValuePairs = nameValuePairs;
		
		new LongRunningPostIO().execute();	
	}

	private class LongRunningGetIO extends AsyncTask<Void, Void, String> {
		protected String getASCIIContentFromEntity(HttpEntity entity)
				throws IllegalStateException, IOException {
			InputStream in = entity.getContent();
			StringBuffer out = new StringBuffer();
			int n = 1;
			while (n > 0) {
				byte[] b = new byte[4096];
				n = in.read(b);
				if (n > 0)
					out.append(new String(b, 0, n));
			}
			return out.toString();
		}

		@Override
		protected String doInBackground(Void... params) {
			HttpClient httpClient = new DefaultHttpClient();
			HttpContext localContext = new BasicHttpContext();
			HttpGet httpGet = new HttpGet("http://" + serverURL + uri);
			String text = null;
			try {
				HttpResponse response = httpClient.execute(httpGet, localContext);
				HttpEntity entity = response.getEntity();
				text = getASCIIContentFromEntity(entity);
			} catch (Exception e) {
				return e.getLocalizedMessage();
			}
			return text;
		}

		protected void onPostExecute(String results) {
			if (results != null) {
				try {
					if(locListener != null) {
						locListener.processServerResults(results);
					}
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		}
	}
	
	private class LongRunningPostIO extends AsyncTask<Void, Void, String> {
		protected String getASCIIContentFromEntity(HttpEntity entity)
				throws IllegalStateException, IOException {
			InputStream in = entity.getContent();
			StringBuffer out = new StringBuffer();
			int n = 1;
			while (n > 0) {
				byte[] b = new byte[4096];
				n = in.read(b);
				if (n > 0)
					out.append(new String(b, 0, n));
			}
			return out.toString();
		}

		@Override
		protected String doInBackground(Void... params) {
			HttpClient httpClient = new DefaultHttpClient();
			HttpPost httppost = new HttpPost("http://" + serverURL + uri);
			String text = null;
			try {
			    httppost.setEntity(new UrlEncodedFormEntity(nameValuePairs));
			    HttpResponse response = httpClient.execute(httppost);
				HttpEntity entity = response.getEntity();
				text = getASCIIContentFromEntity(entity);
			} catch (Exception e) {
				return e.getLocalizedMessage();
			}
			return text;
		}

		protected void onPostExecute(String results) {
			if (results != null) {
				try {
					if(locListener != null) {
						locListener.processServerResults(results);
					}
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		}
	}
}
