<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
    <link type="text/css" href="gaman.CSS" rel="/img/gaman.css">
  </head>
  <body>
      %samlagning = 0
      %for x in kt:
        %samlagning = samlagning + int(x)
      % end
      <h2>Þvermál kennitölunar {{kt}} er {{samlagning}}</h2>
    <a href="/">Lidur B</a>
</body>
</html>
