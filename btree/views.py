import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view

from binarytree import build
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

from .helper import get_bfs, search, connect_nodes_util


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def height(req, **kwargs):
    body_unicode = req.body.decode('utf-8')
    body = json.loads(body_unicode)
    tree_data = body['toTree']

    tree = build(tree_data)

    return JsonResponse({"height": tree.height})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def neighbors(req, **kwargs):
    body_unicode = req.body.decode('utf-8')
    body = json.loads(body_unicode)
    tree_data = body['toTree']
    to_search = body['node']

    tree = build(tree_data)
    connect_nodes_util(tree)
    connect_nodes_util(tree, False)

    search(tree, tree, to_search)

    if hasattr(tree, "found_node"):
        return JsonResponse({
            "neighbors": {
                "left": tree.found_node.leftNeighbour,
                "right": tree.found_node.rightNeighbour
            }
        })

    return HttpResponseNotFound(f"{to_search} wasn't found in the tree")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def bfs(req, **kwargs):
    body_unicode = req.body.decode('utf-8')
    body = json.loads(body_unicode)
    tree_data = body['toTree']

    tree = build(tree_data)

    return JsonResponse({"bfs": get_bfs(tree)})
