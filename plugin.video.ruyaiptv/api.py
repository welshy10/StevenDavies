# -*- coding: utf-8 -*-
#------------------------------------------------------------
# API for RuYa IPTV
# Version 1.0.1
#------------------------------------------------------------
# Changes
# 1.0.1 Added quality selector for movies 
#------------------------------------------------------------

import os
import sys
import urlparse
import plugintools

import urllib

def get_base_url():
    return "http://"+plugintools.get_setting("server")+"/ruyaserver/"

# ---------------------------------------------------------------------------------------------------------
#  users
# ---------------------------------------------------------------------------------------------------------

def login(server,username,password):
    plugintools.log("ruyaiptv.api login server="+server+", username="+username+", password="+password)

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"users/login.php")
    service_parameters = urllib.urlencode({'username':username,'password':password})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )
    return body

# ---------------------------------------------------------------------------------------------------------
#  movies
# ---------------------------------------------------------------------------------------------------------

def get_recent_movies(token,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.get_recent_movies")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"movies/get_recent_movies.php")
    service_parameters = urllib.urlencode({'token':token,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_recent_movies body="+repr(body))
    items = parse_movies(body)
    plugintools.log("ruyaiptv.api.get_recent_movies items="+repr(items))

    return items

def get_latest_releases(token,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.get_latest_releases")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"movies/get_latest_releases.php")
    service_parameters = urllib.urlencode({'token':token,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_latest_releases body="+repr(body))
    items = parse_movies(body)
    plugintools.log("ruyaiptv.api.get_latest_releases items="+repr(items))

    return items

def movie_search(token,terms,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.movie_search")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"movies/movie_search.php")
    service_parameters = urllib.urlencode({'token':token,'q':terms,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.movie_search body="+repr(body))
    items = parse_movies(body)
    plugintools.log("ruyaiptv.api.movie_search items="+repr(items))

    return items

def get_hot_movies(token,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.get_hot_movies")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"movies/get_hot_movies.php")
    service_parameters = urllib.urlencode({'token':token,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_hot_movies body="+repr(body))
    items = parse_movies(body)
    plugintools.log("ruyaiptv.api.get_hot_movies items="+repr(items))

    return items

def get_movies_by_letter(token,letter,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.get_movies_by_letter")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"movies/get_movies_by_letter.php")
    service_parameters = urllib.urlencode({'token':token,'letter':letter,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_movies_by_letter body="+repr(body))
    items = parse_movies(body)
    plugintools.log("ruyaiptv.api.get_movies_by_letter items="+repr(items))

    return items

def get_movie_genres(token):
    plugintools.log("ruyaiptv.api.get_movie_genres")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"movies/get_movie_genres.php")
    service_parameters = urllib.urlencode({'token':token})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_movie_genres body="+repr(body))
    items = parse_movie_genres(body)
    plugintools.log("ruyaiptv.api.get_movie_genres items="+repr(items))

    return items

def get_movies_by_genre(token,genre,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.get_movies_by_genre")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"movies/get_movies_by_genre.php")
    service_parameters = urllib.urlencode({'token':token,'genre':genre,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_movies_by_genre body="+repr(body))
    items = parse_movies(body)
    plugintools.log("ruyaiptv.api.get_movies_by_genre items="+repr(items))

    return items

# ---------------------------------------------------------------------------------------------------------
#  tvshows
# ---------------------------------------------------------------------------------------------------------

def get_recent_episodes(token,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.get_recent_episodes")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"tvshows/get_recent_episodes.php")
    service_parameters = urllib.urlencode({'token':token,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_recent_episodes body="+repr(body))
    items = parse_tvshow_episodes(body)
    plugintools.log("ruyaiptv.api.get_recent_episodes items="+repr(items))

    return items

def get_updated_tvshows(token,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.get_updated_tvshows")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"tvshows/get_updated_tvshows.php")
    service_parameters = urllib.urlencode({'token':token,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_updated_tvshows body="+repr(body))
    items = parse_tvshows(body)
    plugintools.log("ruyaiptv.api.get_updated_tvshows items="+repr(items))

    return items

def tvshow_search(token,terms,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.tvshow_search")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"tvshows/tvshow_search.php")
    service_parameters = urllib.urlencode({'token':token,'q':terms,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.tvshow_search body="+repr(body))
    items = parse_tvshows(body)
    plugintools.log("ruyaiptv.api.tvshow_search items="+repr(items))

    return items

def get_tvshows_by_letter(token,letter,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.get_tvshows_by_letter")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"tvshows/get_tvshows_by_letter.php")
    service_parameters = urllib.urlencode({'token':token,'letter':letter,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_tvshows_by_letter body="+repr(body))
    items = parse_tvshows(body)
    plugintools.log("ruyaiptv.api.get_tvshows_by_letter items="+repr(items))

    return items

def get_tvshow_seasons(token,tvshow,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.get_tvshow_seasons")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"tvshows/get_tvshow_seasons.php")
    service_parameters = urllib.urlencode({'token':token,'tvshow':tvshow,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_tvshow_seasons body="+repr(body))
    items = parse_tvshow_seasons(body)
    plugintools.log("ruyaiptv.api.get_tvshow_seasons items="+repr(items))

    return items

def get_tvshow_episodes(token,tvshow,season,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.get_tvshow_episodes")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"tvshows/get_tvshow_episodes.php")
    service_parameters = urllib.urlencode({'token':token,'tvshow':tvshow,'season':season,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_tvshow_episodes body="+repr(body))
    items = parse_tvshow_episodes(body)
    plugintools.log("ruyaiptv.api.get_tvshow_episodes items="+repr(items))

    return items

def get_tvshow_genres(token):
    plugintools.log("ruyaiptv.api.get_tvshow_genres")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"tvshows/get_tvshow_genres.php")
    service_parameters = urllib.urlencode({'token':token})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_tvshow_genres body="+repr(body))
    items = parse_tvshow_genres(body)
    plugintools.log("ruyaiptv.api.get_tvshow_genres items="+repr(items))

    return items

def get_tvshows_by_genre(token,genre,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.get_tvshows_by_genre")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"tvshows/get_tvshows_by_genre.php")
    service_parameters = urllib.urlencode({'token':token,'genre':genre,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_tvshows_by_genre body="+repr(body))
    items = parse_tvshows(body)
    plugintools.log("ruyaiptv.api.get_tvshows_by_genre items="+repr(items))

    return items

# ---------------------------------------------------------------------------------------------------------
#  livetv
# ---------------------------------------------------------------------------------------------------------

def get_livetv_genres(token):
    plugintools.log("ruyaiptv.api.get_livetv_genres")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"livetv/get_livetv_genres.php")
    service_parameters = urllib.urlencode({'token':token})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_tvshow_genres body="+repr(body))
    items = parse_livetv_genres(body)
    plugintools.log("ruyaiptv.api.get_tvshow_genres items="+repr(items))

    return items

def get_livetv_packages(token):
    plugintools.log("ruyaiptv.api.get_livetv_packages")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"livetv/get_livetv_packages.php")
    service_parameters = urllib.urlencode({'token':token})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_tvshow_packages body="+repr(body))
    items = parse_livetv_packages(body)
    plugintools.log("ruyaiptv.api.get_tvshow_packages items="+repr(items))

    return items

def get_all_livetv_channels(token,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.get_all_livetv_channels")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"livetv/get_all_livetv_channels.php")
    service_parameters = urllib.urlencode({'token':token,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_all_livetv_channels body="+repr(body))
    items = parse_livetv_channels(body)
    plugintools.log("ruyaiptv.api.get_all_livetv_channels items="+repr(items))

    return items

def get_livetv_channels_by_genre(token,genre,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.get_livetv_channels_by_genre")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"livetv/get_livetv_channels_by_genre.php")
    service_parameters = urllib.urlencode({'token':token,'genre':genre,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_livetv_channels_by_genre body="+repr(body))
    items = parse_livetv_channels(body)
    plugintools.log("ruyaiptv.api.get_livetv_channels_by_genre items="+repr(items))

    return items

def get_livetv_channels_by_package(token,package,num_page="",per_page=""):
    plugintools.log("ruyaiptv.api.get_livetv_channels_by_package")

    # Service call
    service_url = urlparse.urljoin(get_base_url(),"livetv/get_livetv_channels_by_package.php")
    service_parameters = urllib.urlencode({'token':token,'package':package,'num_page':num_page,'per_page':per_page})
    body , response_headers = plugintools.read_body_and_headers( service_url , post=service_parameters )

    # Response parsing
    plugintools.log("ruyaiptv.api.get_livetv_channels_by_package body="+repr(body))
    items = parse_livetv_channels(body)
    plugintools.log("ruyaiptv.api.get_livetv_channels_by_package items="+repr(items))

    return items

def get_livetv_url(token,url):
    plugintools.log("ruyaiptv.api.get_livetv_url")

    import base64
    plugintools.log("ruyaiptv.api.get_livetv_url url="+url)
    url = base64.b64decode(url)
    plugintools.log("ruyaiptv.api.get_livetv_url url="+url)

    # Service call
    body , response_headers = plugintools.read_body_and_headers( url )
    plugintools.log("ruyaiptv.api.get_livetv_url body="+body)

    mediaurl = base64.b64decode(body)
    plugintools.log("ruyaiptv.api.get_livetv_url mediaurl="+mediaurl)

    return mediaurl

# ---------------------------------------------------------------------------------------------------------
#  parsers
# ---------------------------------------------------------------------------------------------------------

def parse_movies(body):

    patron = "<movie>(.*?)</movie>"
    movies = plugintools.find_multiple_matches(body,patron)

    items = []
    for movie in movies:
        item = {}
        item["title"] = plugintools.find_single_match(movie,"<title>([^<]+)</title>")

        item["url"] = ""
        low_quality_url = plugintools.find_single_match(movie,"<low_quality_url>([^<]+)</low_quality_url>")
        if low_quality_url != "":
            item["url"] = item["url"] + low_quality_url

        high_quality_url = plugintools.find_single_match(movie,"<high_quality_url>([^<]+)</high_quality_url>")
        if high_quality_url != "":
            if item["url"]!="":
                item["url"] = item["url"] + "|"
            item["url"] = item["url"] + high_quality_url

        # There can be one quality (low) or two qualities (low|high). If there is none of them, add the original quality as the only one
        if item["url"]=="":
            item["url"] = plugintools.find_single_match(movie,"<url>([^<]+)</url>")

        item["thumbnail"] = plugintools.find_single_match(movie,"<thumbnail>([^<]+)</thumbnail>")
        item["fanart"] = plugintools.find_single_match(movie,"<fanart>([^<]+)</fanart>")
        item["plot"] = plugintools.find_single_match(movie,"<plot>([^<]+)</plot>")

        if item["title"]!="" and item["url"]!="":
            items.append(item)

    return items

def parse_movie_genres(body):

    patron = "<genre>([^<]+)</genre>"
    genres = plugintools.find_multiple_matches(body,patron)

    items = []
    for genre in genres:
        item = {}
        item["title"] = genre
        items.append(item)

    return items

def parse_tvshows(body):
    plugintools.log("ruyaiptv.api.parse_tvshows")

    patron = "<tvshow>(.*?)</tvshow>"
    tvshows = plugintools.find_multiple_matches(body,patron)

    items = []
    for tvshow in tvshows:
        item = {}
        item["title"] = plugintools.find_single_match(tvshow,"<title>([^<]+)</title>")
        item["thumbnail"] = plugintools.find_single_match(tvshow,"<thumbnail>([^<]+)</thumbnail>")
        item["fanart"] = plugintools.find_single_match(tvshow,"<fanart>([^<]+)</fanart>")
        item["plot"] = plugintools.find_single_match(tvshow,"<plot>([^<]+)</plot>")

        if item["title"]!="":
            items.append(item)

    return items

def parse_tvshow_seasons(body):
    plugintools.log("ruyaiptv.api.parse_tvshow_episodes")

    patron = "<season>(.*?)</season>"
    episodes = plugintools.find_multiple_matches(body,patron)

    items = []
    for episode in episodes:
        item = {}
        item["title"] = plugintools.find_single_match(episode,"<title>([^<]+)</title>")
        item["thumbnail"] = plugintools.find_single_match(episode,"<thumbnail>([^<]+)</thumbnail>")
        item["fanart"] = plugintools.find_single_match(episode,"<fanart>([^<]+)</fanart>")
        item["plot"] = ""

        if item["title"]!="":
            items.append(item)

    return items

def parse_tvshow_episodes(body):
    plugintools.log("ruyaiptv.api.parse_tvshow_episodes")

    patron = "<episode>(.*?)</episode>"
    episodes = plugintools.find_multiple_matches(body,patron)

    items = []
    for episode in episodes:
        item = {}
        item["title"] = plugintools.find_single_match(episode,"<title>([^<]+)</title>")
        item["thumbnail"] = plugintools.find_single_match(episode,"<thumbnail>([^<]+)</thumbnail>")
        item["fanart"] = plugintools.find_single_match(episode,"<fanart>([^<]+)</fanart>")
        item["plot"] = plugintools.find_single_match(episode,"<plot>([^<]+)</plot>")

        item["url"] = ""
        low_quality_url = plugintools.find_single_match(episode,"<low_quality_url>([^<]+)</low_quality_url>")
        if low_quality_url != "":
            item["url"] = item["url"] + low_quality_url

        high_quality_url = plugintools.find_single_match(episode,"<high_quality_url>([^<]+)</high_quality_url>")
        if high_quality_url != "":
            if item["url"]!="":
                item["url"] = item["url"] + "|"
            item["url"] = item["url"] + high_quality_url

        # There can be one quality (low) or two qualities (low|high). If there is none of them, add the original quality as the only one
        if item["url"]=="":
            item["url"] = plugintools.find_single_match(episode,"<url>([^<]+)</url>")

        if item["title"]!="":
            items.append(item)

    return items

def parse_tvshow_genres(body):

    patron = "<genre>([^<]+)</genre>"
    genres = plugintools.find_multiple_matches(body,patron)

    items = []
    for genre in genres:
        item = {}
        item["title"] = genre
        items.append(item)

    return items

def parse_livetv_genres(body):

    patron = "<genre>([^<]+)</genre>"
    genres = plugintools.find_multiple_matches(body,patron)

    items = []
    for genre in genres:
        item = {}
        item["title"] = genre
        items.append(item)

    return items

def parse_livetv_packages(body):

    patron = "<package>([^<]+)</package>"
    packages = plugintools.find_multiple_matches(body,patron)

    items = []
    for package in packages:
        item = {}
        item["title"] = package
        items.append(item)

    return items

def parse_livetv_channels_by_genre(body,genre):

    patron = "<group[^<]+<name>"+genre+"</name>(.*?)</group>"
    block = plugintools.find_single_match(body,patron)

    return parse_livetv_channels(block)

def parse_livetv_channels(body):

    patron = "<channel>(.*?)</channel>"
    channels = plugintools.find_multiple_matches(body,patron)

    items = []
    for channel in channels:

        adult = plugintools.find_single_match(channel,"<adult>([^<]+)</adult>")

        if plugintools.get_setting("show_adult")=="true" or (plugintools.get_setting("show_adult")=="false" and adult!="true"):
            item = {}
            item["title"] = plugintools.find_single_match(channel,"<name>([^<]+)</name>")
            item["url"] = plugintools.find_single_match(channel,"<stream_url>([^<]+)</stream_url>")
            if item["url"].startswith("movie://"):
                item["url"] = item["url"].replace("movie://","")
            item["thumbnail"] = plugintools.find_single_match(channel,"<piconname>([^<]+)</piconname>")
            item["plot"] = plugintools.find_single_match(channel,"<plot>([^<]+)</plot>")
            item["fanart"] = adult

            if item["title"]!="" and item["url"]!="":
                print "item="+str(item)
                items.append(item)
            else:
                print "item without title "+str(item)

    return items

# ---------------------------------------------------------------------------------------------------------
#  fixme: old test function
# ---------------------------------------------------------------------------------------------------------

def read_server_response(url):

    if url=="movies":
        f = open( os.path.join( plugintools.get_runtime_path(),"api-movies.xml") ,"r")
        body = f.read()
        f.close()
    elif url=="tvshows":
        f = open( os.path.join( plugintools.get_runtime_path(),"api-tvshows.xml") ,"r")
        body = f.read()
        f.close()
    elif url=="livetv":
        f = open( os.path.join( plugintools.get_runtime_path(),"api-livetv.xml") ,"r")
        body = f.read()
        f.close()

    return body