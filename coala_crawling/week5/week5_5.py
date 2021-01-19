from urllib.request import urlretrieve

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

src = "https://movie-phinf.pstatic.net/20191030_118/1572411669676j0Arb_JPEG/movie_image.jpg?type=m203_290_2"
urlretrieve(src, "poster.png")
