import json

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from .helper import get_bfs, search, connect_nodes_util
from binarytree import build


class APITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.client.login(username='test', password='test')

    def test_height_of_2_levels(self):
        payload = {'toTree': [10, 8, 2, 3]}

        response = self.client.post(
                        reverse('btree:height'),
                        payload,
                        format='json'
                    )
        body_unicode = response.getvalue().decode('utf-8')
        body = json.loads(body_unicode)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body['height'], 2)

    def test_height_of_3_levels(self):
        payload = {'toTree': [1, 2, 3, 4, 5, 6, 7, 8]}

        response = self.client.post(
                        reverse('btree:height'),
                        payload,
                        format='json'
                    )
        body_unicode = response.getvalue().decode('utf-8')
        body = json.loads(body_unicode)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body['height'], 3)

    def test_height_of_4_levels(self):
        payload = {'toTree': [2, 11, 5, 5, 6, 9, 4, 7, 2, 13, 8, 9, 1, 4, 22, 35]}

        response = self.client.post(
                        reverse('btree:height'),
                        payload,
                        format='json'
                    )
        body_unicode = response.getvalue().decode('utf-8')
        body = json.loads(body_unicode)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body['height'], 4)

    def test_long_bfs(self):
        example = [2, 11, 5, 5, 6, 9, 4, 7, 2, 13, 8, 9, 1, 4, 22, 35]
        payload = {'toTree': example}

        response = self.client.post(
                        reverse('btree:bfs'),
                        payload,
                        format='json'
                    )
        body_unicode = response.getvalue().decode('utf-8')
        body = json.loads(body_unicode)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body['bfs'], example)

    def test_short_bfs(self):
        example = [-3, -4, 1]
        payload = {'toTree': example}

        response = self.client.post(
                        reverse('btree:bfs'),
                        payload,
                        format='json'
                    )
        body_unicode = response.getvalue().decode('utf-8')
        body = json.loads(body_unicode)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body['bfs'], example)

    def test_neighbors_short(self):
        example = [1, 2, 3, 4, 5, 6, 7, 8]
        result = {
            "left": 3,
            "right": None
        }
        payload = {'toTree': example, "node": 2}

        response = self.client.post(
                        reverse('btree:neighbors'),
                        payload,
                        format='json'
                    )
        body_unicode = response.getvalue().decode('utf-8')
        body = json.loads(body_unicode)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body['neighbors'], result)

    def test_neighbors_long(self):
        example = [29, 18, 74, 6, 50, 76, 51, 80, 71]
        result = {
            "left": 51,
            "right": 50
        }
        payload = {'toTree': example, "node": 76}

        response = self.client.post(
                        reverse('btree:neighbors'),
                        payload,
                        format='json'
                    )
        body_unicode = response.getvalue().decode('utf-8')
        body = json.loads(body_unicode)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body['neighbors'], result)

    def test_neighbors_not_found(self):
        example = [29, 18, 74, 6, 50, 76, 51, 80, 71]
        node = 100
        result = {
            "left": 51,
            "right": 50
        }
        payload = {'toTree': example, "node": node}

        response = self.client.post(
                        reverse('btree:neighbors'),
                        payload,
                        format='json'
                    )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(
                response.getvalue().decode('utf-8'),
                f"{node} wasn't found in the tree"
            )


class HelperTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.client.login(username='test', password='test')

    def test_find_item(self):
        items = [10, 8, 2, 3]

        tree = build(items)

        search(tree, tree, 10)
        self.assertEqual(tree.found_node.value, 10)

        search(tree, tree, 8)
        self.assertEqual(tree.found_node.value, 8)

        search(tree, tree, 2)
        self.assertEqual(tree.found_node.value, 2)

        search(tree, tree, 3)
        self.assertEqual(tree.found_node.value, 3)

    def test_get_bfs_metho(self):
        items = [2, 11, 5, 5, 6, 9, 4, 7, 2, 13, 8, 9, 1, 4, 22, 35]

        tree = build(items)

        bfs = get_bfs(tree)
        self.assertEqual(bfs, items)
