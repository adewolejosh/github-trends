
import requests
import datetime

from .serializers import SearchSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class GithubTrendsView(APIView):
    """
    A View which displays the result of the analysed github trending repos
    """

    def get(self, request):
        try:
            # calculating thirty days ago
            current_date, t_minus_day = datetime.date.today(), datetime.timedelta(-30)
            thirty_days_ago = current_date + t_minus_day

            # url parameters
            date, per_page = thirty_days_ago.strftime("%Y-%m-%d"), 100
            url = f'https://api.github.com/search/repositories?q=created:>{date}&sort=stars&order=desc&per_page={per_page}'

            # check if you're within your rate limit as this is an unauthenticated API
            rate_url = 'https://api.github.com/ratelimit/'
            rate_limit = requests.get(rate_url)
            rate = rate_limit.headers.get('X-RateLimit-Remaining')
            if int(rate) <= 0:
                raise TimeoutError("API rate Limit exceeded for an hour, please try again later!")

            # request to api.github.com/search
            trending_repos = requests.get(url)

            # response from request; converted to json for ease
            response = trending_repos.json()
            # locating the needed result(i.e repositories)
            items = response['items']

            # passing the result to the serializer to analyse and yield result
            serializer = SearchSerializer(items, many=True)
            # returning the result gotten from above with a status 200
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ConnectionError or TimeoutError or KeyError:
            raise
