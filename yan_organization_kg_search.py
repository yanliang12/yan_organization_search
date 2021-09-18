###########yan_organization_kg_search.py############
import jessica_es
import jessica_neo4j 
import yan_page_parsed_to_triplet

import yan_image_embedding
import jim_es_vector_search

jessica_neo4j.start_neo4j(
	http_port = "5611", 
	bolt_port = "4971")
neo4j_session = jessica_neo4j.create_neo4j_session(
	bolt_port = "4971")

es_session = jessica_es.start_es(
	es_path = "/dcd_data/es/elasticsearch_organization",
	es_port_number = "9344")

'''
jessica_es.start_kibana(
	kibana_path = '/jessica/kibana-6.7.1-linux-x86_64',
	kibana_port_number = "3641",
	es_port_number = "9344",
	)
'''

def search_by_page_url_hash_and_ingest_to_neo4j(
	page_url_hash,
	):
	output = jessica_es.search_doc_by_filter(
		index_name = 'organization',
		field_name = 'page_url_hash',
		entity_name = page_url_hash,
		es_session = es_session,
		return_entity_max_number = 1)
	parsed = output[0]['parsed']
	page_url = output[0]['page_url']
	triplets = yan_page_parsed_to_triplet.parsed_info_2_kg_triplets(parsed)
	jessica_neo4j.ingest_knowledge_triplets_to_neo4j(
		triplets, 
		neo4j_session)
	return page_url

'''
yan_organization_kg_search.search_organization_by_name(
	organization_name = "Department of Community Development",
	)
'''

def search_organization_by_logo(
	organization_logo_path,
	):
	query_vector = yan_image_embedding.image_to_vector(organization_logo_path)
	output = jim_es_vector_search.search_by_vector(
		index_name = 'organization_logo_embedding',
		vector_field_name = 'logo_embedding',
		query_vector = query_vector,
		es_session = es_session,
		similarity_measure = 'euclidean',
		)
	page_url = search_by_page_url_hash_and_ingest_to_neo4j(
		output[0]['page_url_hash'],
		)
	return page_url

'''
yan_organization_kg_search.search_organization_by_logo(
	'/dcd_data/linkedin/group 42 logo-og-image.jpg'
	)
'''



def search_organization_by_name(
	organization_name,
	):
	output = jessica_es.search_doc_by_match(
		index_name = 'organization',
		entity_name = organization_name,
		field_name = 'organization_name',
		es_session = es_session,
		return_entity_max_number = 1,
		return_entity_min_score = 0.1,
		)
	parsed = output[0]['parsed']
	page_url = output[0]['page_url']
	triplets = yan_page_parsed_to_triplet.parsed_info_2_kg_triplets(parsed)
	jessica_neo4j.ingest_knowledge_triplets_to_neo4j(
		triplets, 
		neo4j_session)
	return page_url

###########yan_organization_kg_search.py############