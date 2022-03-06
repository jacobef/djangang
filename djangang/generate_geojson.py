import os

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangang.settings")
django.setup()

from django.db.models import QuerySet

from rental.models import Tool


def generate_geojson():
    def generate_tool_geojson(tool: Tool):
        return f"""        {{
            "type": "Feature",
            "properties": {{}},
            "geometry": {{
                "type": "Point",
                "coordinates": [
                    {tool.location[0]},
                    {tool.location[1]}
                ]
            }}
        }}"""

    def generate_map_geojson(tools: QuerySet):
        features_content = ""
        for tool in tools:
            features_content += generate_tool_geojson(tool)
            features_content += ',\n'
        return f"""{{
    "type": "FeatureCollection",
    "features": [
{features_content}
    ]
}}"""

    tools = Tool.objects.all()
    return generate_map_geojson(tools)
