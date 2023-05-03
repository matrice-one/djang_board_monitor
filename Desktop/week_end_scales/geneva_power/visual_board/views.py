from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Company, BoardMember
from collections import deque



class GetNetworkDataView(APIView):
    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('search_term', '').strip()
        # SHOULD IMPLEMENT A VIEWSET + SERIALIZER INSTEAD TO REMAIN CLEANER AND MORE MODULABLE
        max_nodes = int(request.GET.get('max_nodes', 30))

        if not search_term:
            return JsonResponse({'error': 'No search term provided'})

        if not max_nodes:
            max_nodes = 4

        # Find the starting node (either a Company or a BoardMember)
        company = Company.objects.filter(name__icontains=search_term).first()
        board_member = BoardMember.objects.filter(name_and_surname__icontains=search_term).first()

        if not company and not board_member:
            return JsonResponse({'error': 'No matching company or board member found'})

        start_node = company or board_member

        # BFS algorithm to find the closest nodes
        visited = set()
        queue = deque([(start_node)])
        nodes_counter = 0

        while queue and nodes_counter <= max_nodes:
            node = queue.popleft()

            if node not in visited:
                visited.add(node)

                if isinstance(node, Company):
                    for bm in node.board_members.all():
                        if nodes_counter < max_nodes:
                            queue.append(bm)
                            nodes_counter += 1
                        else:
                            break
                        queue.append(bm)
                else:  # isinstance(node, BoardMember)
                    for c in node.company_set.all():
                        if nodes_counter < max_nodes:
                            queue.append(c)
                            nodes_counter += 1
                        else:
                            break
        # Prepare the data for D3.js
        nodes = []
        links = []

        for node in visited:
            if isinstance(node, Company):
                nodes.append({'id': f'c{node.id}', 'label': node.name, 'type': 'company'})
            else:  # isinstance(node, BoardMember)
                nodes.append({'id': f'b{node.id}', 'label': node.name_and_surname, 'type': 'board_member'})

        for node in visited:
            if isinstance(node, Company):
                for board_member in node.board_members.all():
                    if board_member in visited:
                        links.append({'source': f'c{node.id}', 'target': f'b{board_member.id}'})

        data = {'nodes': nodes, 'links': links}
        return Response(data)
