def triangulate(points):
    """ Given points in (x,y, signal) format, approximate the position (x,y).

        Reading:
        * http://stackoverflow.com/questions/10329877/how-to-properly-triangulate-gsm-cell-towers-to-get-a-location
        * http://www.neilson.co.za/?p=364
        * http://gis.stackexchange.com/questions/40660/trilateration-algorithm-for-n-amount-of-points
        * http://gis.stackexchange.com/questions/2850/what-algorithm-should-i-use-for-wifi-geolocation
    """
    # Weighted signal strength
    ws = sum(p[2] for p in points)
    print ws
    points = tuple( (x,y,signal/ws) for (x,y,signal) in points )
    # Approximate
    return (
        sum(p[0]*p[2] for p in points), # x
        sum(p[1]*p[2] for p in points) # y
    )


print(triangulate([
    (14.2565389, 48.2248439, 150.00),
    (14.2637736, 48.2331576, 55.00),
    (14.2488966, 48.232513, 55.00),
    (14.2488163, 48.2277972, 99.00),
    (14.2647612, 48.2299558, 0.00),
]))