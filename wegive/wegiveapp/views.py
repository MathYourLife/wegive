from django.shortcuts import render
from . import models
from . import forms

# Create your views here.

def match_charity(name="", tags="", near_x=0.0, near_y=0.0, near_distance=0.0):
    """
    Usage: match_charity(name="", tags="", near_x=0.0, near_y=0.0)
    Searches for charities with the given search terms.

    Parameters:
    string name: name of the charity
    string tags: csv of tags. Not implemented
    float near_x: origin x coordinate for a location based search
    float near_y: origin y coordinate for a location based search
    float near_distance: radius for a location based search.

    Returns:
    The resulting query set.
    """
    # construct kwargs
    kwargs = {}
    if name != "":
        kwargs["name__contains"] = name
    if tags != "":                               # NOT IMPLEMENTED
        pass
    # parentheses here for implicit line completion
    if (near_x != 0 and near_y != 0 and near_distance != 0 and
        near_x != "" and near_y != "" and near_distance != ""):
        max_y = float(near_y) + float(near_distance)
        min_x = float(near_x) - float(near_distance)
        min_y = float(near_y) - float(near_distance)
        max_x = float(near_x) + float(near_distance)

        kwargs["location_x__gte"] = min_x
        kwargs["location_x__lte"] = max_x
        kwargs["location_y__gte"] = min_y
        kwargs["location_y__lte"] = max_y

    # get query set
    results_qset = models.Charity.objects.filter(**kwargs)

    return results_qset

def search(request):
    """
    Search for charities.
    When accessed through GET, gives a search form.
    When accessed through POST, gives a table with search results. Each result
    will link to a select request.
    """
    if request.method == "POST":
        # TODO: near me test
        res = match_charity(
            name=request.POST["name"], near_x=request.POST["location_x"],
            near_y=request.POST["location_y"], near_distance=request.POST["radius"])
        return render(request, "html/search-results.html", {"res": res})
    else:
        form = forms.SearchForm()
        return render(request, "html/search.html", {"form": form})

def select(request):
    pass

def pay(request):
    pass
