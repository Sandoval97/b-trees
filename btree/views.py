import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def height(req, **kwargs):
    return JsonResponse({})

@csrf_exempt
def neighbors(req, **kwargs):
    body_unicode = req.body.decode('utf-8')
    body = json.loads(body_unicode)
    tree = body['toTree']
    node = body['node']

    index_node = tree.index(node)
    left = None
    right = None

    for number in range(index_node, len(tree) ):
        if tree[number] % 2 == 0 and node != tree[number]:
            right = tree[number]
            break

    new_tree = tree[:index_node]
    new_tree.reverse()

    for number in new_tree:
        if number % 2 == 0 and node != number:
            left = number
            break
    
    return JsonResponse({  "left": left, "right": right })

def bfs(req, **kwargs):
    return JsonResponse({})