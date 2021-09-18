#####################server_path.py#####################
import time
import logging
import argsparser
from flask import *
from flask_restplus import *

import yan_organization_kg_search

######

ns = Namespace('knowledge_graph', description='')
args = argsparser.prepare_args()

parser = ns.parser()
parser.add_argument('organization_name', type=str, location='json')
parser.add_argument('organization_logo_path', type=str, location='json')

###############
req_fields = {
	'organization_name': fields.String(),
	}
jessica_api_req = ns.model('knowledge_graph', req_fields)

rsp_fields = {\
	'status':fields.String,\
	'source_url':fields.String,\
	'running_time':fields.Float\
	}
jessica_api_rsp = ns.model('knowledge_graph', rsp_fields)

@ns.route('/organization_search/organization_name')
class jessica_api(Resource):
	def __init__(self, *args, **kwargs):
		super(jessica_api, self).__init__(*args, **kwargs)
	@ns.marshal_with(jessica_api_rsp)
	@ns.expect(jessica_api_req)
	def post(self):		
		start = time.time()
		try:			
			args = parser.parse_args()
			output = {}
			output['source_url'] = yan_organization_kg_search.search_organization_by_name(
				organization_name = args["organization_name"],
				)
			output['status'] = 'success'
			output['running_time'] = float(time.time()- start)
			return output, 200
		except Exception as e:
			output = {}
			output['status'] = str(e)
			output['running_time'] = float(time.time()- start)
			return output


###############

req_fields1 = {
	'organization_logo_path': fields.String(),
	}
jessica_api_req1 = ns.model('knowledge_graph', req_fields1)

rsp_fields1 = {\
	'status':fields.String,\
	'source_url':fields.String,\
	'running_time':fields.Float\
	}
jessica_api_rsp1 = ns.model('knowledge_graph', rsp_fields1)

@ns.route('/organization_search/organization_logo')
class jessica_api1(Resource):
	def __init__(self, *args, **kwargs):
		super(jessica_api1, self).__init__(*args, **kwargs)
	@ns.marshal_with(jessica_api_rsp1)
	@ns.expect(jessica_api_req1)
	def post(self):		
		start = time.time()
		try:			
			args = parser.parse_args()
			output = {}
			output['source_url'] = yan_organization_kg_search.search_organization_by_logo(
					organization_logo_path = args["organization_logo_path"],
					)
			output['status'] = 'success'
			output['running_time'] = float(time.time()- start)
			return output, 200
		except Exception as e:
			output = {}
			output['status'] = str(e)
			output['running_time'] = float(time.time()- start)
			return output

#####################server_path.py#####################