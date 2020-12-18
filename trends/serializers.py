
from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    """
    Serializer that manipulates the data from GithubTrendViews
    """

    items = serializers.SerializerMethodField(read_only=True)

    def get_items(self, obj):
        # languages list to output- defined
        lan = []
        # sorted languages, number of repo. and repo. array output- defined
        arr = []

        # loop through each item in the response from the API
        for i in range(len(obj)):
            # loop through each dict in an item - to find language
            for k, v in obj[i].items():
                # Condition for if a key is language but the value is null
                if k == "language" and v is None:
                    # first time ? then add
                    if k == "language" and "None" not in lan:
                        lan.append("None")
                        b = {str(k): "None", "count": 1, "projects": []}
                        b['projects'].append(obj[i])
                        arr.append(b)
                    # consequent times ? find item add
                    elif k == "language" and "None" in lan:
                        for y in range(len(arr)):
                            for ke, va in arr[y].items():
                                if ke == "language" and va == "None":
                                    arr[y]['count'] += 1
                                    arr[y]['projects'].append(obj[i])
                    continue
                # Condition for if a key is language and its an actual language
                if k == "language" and v is not None:
                    # first time ? then add
                    if k == "language" and v not in lan:
                        lan.append(str(v))
                        a = {str(k): str(v), "count": 1, "projects": []}
                        a['projects'].append(obj[i])
                        arr.append(a)
                    # consequent times ? find item add
                    elif k == "language" and v in lan:
                        for x in range(len(arr)):
                            for key, value in arr[x].items():
                                if key == k and value == v:
                                    arr[x]['count'] += 1
                                    arr[x]['projects'].append(obj[i])

        return {"List of Languages": lan}, {"Sorted languages, number of repo, repos attached to each": arr}
