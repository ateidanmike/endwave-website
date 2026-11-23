Map outlines for the network map in `script.js` (`const GEO`).

Country borders: Natural Earth 1:50m via `world-atlas@2`. Lakes: `@geo-maps/earth-lakes-1km`.

    npm i world-atlas@2 topojson-client @geo-maps/earth-lakes-1km
    node --max-old-space-size=4096 gen.js   # writes map.json; paste into GEO in script.js
