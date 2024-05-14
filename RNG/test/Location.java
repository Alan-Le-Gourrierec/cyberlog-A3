package test;

public class Location
{
    private final double latitude;
    private final double longitude;
    public Location(double latitude, double longitude)
    {
        this.latitude = latitude;
        this.longitude = longitude;
    }
    public double distance(Location location)
    {
        double R = 6371 * Math.pow(10, 3);
        double dlat = ((this.latitude + location.latitude)* Math.PI) / 180;
        double dlon = ((this.longitude + location.longitude)* Math.PI) / 180;
        double a = Math.pow(Math.sin(dlat/2), 2) + Math.pow(Math.sin(dlon/2),2) * Math.cos(dlat) * Math.cos(location.latitude);
        return 2 * R * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
    }
}