# yan_organization_search

## pull
```
docker pull yanliang12/yan_organization_search:1.0.1
```

## run

```
docker run -it ^
-p 0.0.0.0:9344:9344 ^
-p 0.0.0.0:3641:3641 ^
-p 0.0.0.0:5611:5611 ^
-p 0.0.0.0:4971:4971 ^
-p 0.0.0.0:2644:9000 ^
-v "E:\dcd_data":/dcd_data/ ^
yanliang12/yan_organization_search:1.0.1
```
