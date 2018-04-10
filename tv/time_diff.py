from tv.views import Movies
import datetime

movie = Movies.objects.first()

timediff = datetime.datetime.now() - movie.showtime
print(timediff.seconds)