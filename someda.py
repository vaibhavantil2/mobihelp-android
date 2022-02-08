import com.google.android.gms.ads.identifier.AdvertisingIdClient.Info;


Info adInfo = null;

try {
     adInfo = AdvertisingIdClient.getAdvertisingIdInfo(mContext);
} catch (IOException e) {
     e.printStackTrace();
} catch (GooglePlayServicesAvailabilityException e) {
     e.printStackTrace();
} catch (GooglePlayServicesNotAvailableException e) {
     e.printStackTrace();
}

String AdId = adInfo.getId();
