# -*- coding: utf-8 -*-

############linkedin_company_parsing.py############
import re
import datetime

###########



###########



'''
import pandas

page = pandas.read_json(
	'/dcd_data/linkedin/company_page_list_html/source=g42/8f808f275dcbd4bf341d75f6f6aaca47.json',
	orient = 'records',
	lines = True,
	)

page_html = page['page_html'][0]
page_url = page['page_url'][0]


for m in re.finditer(r'.{0,100}group42ai.{0,100}',
	page_html):
	print(m.group())

for e in parsing_from_list_to_url(
	page_html,
	page_url,
	):
	print(e)

print(page_url)

'''

###########


###########

re_url_attrbites = [
	re.compile(r'linkedin\.com\/(company|school)\/(?P<organization__organization_id__organization_id>[^\/]*?)\/', flags=re.DOTALL),
	re.compile(r'linkedin\.com\/(?P<organization__orgnization_type__orgnization_type>(company|school))\/', flags=re.DOTALL),
	]

re_company_profile = [
	re.compile(r'companyIndustries\"\:\[\"urn\:li\:fs_industry\:(?P<organization__fsd_industry__fsd_industry>\d+)\".{0,30}lcpTreatment', flags=re.DOTALL),
	re.compile(r'phone\"\:\{\"number\"\:\"(?P<organization__organization_phone__phone>.{0,50})\"\,\"', flags=re.DOTALL),
	re.compile(r'\"companyPageUrl\"\:\"(?P<organization__organization_website_url__url>[^\"]*?)\"', flags=re.DOTALL),
	re.compile(r'foundedOn\"\:\{\"year\"\:(?P<organization__funding_time__year>\d+)\,\"', flags=re.DOTALL),
	re.compile(r'tagline\"\:\"(?P<organization__tag_line__text>[^\"]+)\"\,', flags=re.DOTALL),
	re.compile(r'name\"\:\"(?P<organization__organization_name__organization_name>[^\"]*?)\"\,\"fundingData', flags=re.DOTALL),
	re.compile(r'companyType\"\:\{\"localizedName\"\:\"(?P<organization__organization_ownershipe_type__ownershipe_type>[^\"]{1,100})\"\,', flags=re.DOTALL),
	re.compile(r'trendingContentVisibility\"\:\"ALL_EMPLOYEES\"\}\,\"description\"\:\"(?P<organization__overview__text>[^\"]+)\"\,', flags=re.DOTALL),
	re.compile(r'companyEmployeesSearchPageUrl\"\:\"https\:\/\/www\.linkedin\.com\/vsearch\/p\?f_CC\=(?P<organization__fsd_organization__fsd_company>\d+)\"\,\"', flags=re.DOTALL),
	re.compile(r'fs_organizationStockQuote\:\(\d+\,(?P<organization__organization_stock_quote__stock_quote>[^\(\)]*?)\)\"\]', flags=re.DOTALL),
	re.compile(r'\{\"localizedName\"\:\"(?P<industry__industry_name__industry_name>[^\{\}]+)\"\,\"entityUrn\"\:\"urn\:li\:fs_industry\:(?P<industry__fsd_industry__fsd_industry>\d+)\"\,\"\$type\"\:\"com\.linkedin\.voyager\.common\.Industry\"\}', flags=re.DOTALL),
	]


re_geo_block = re.compile(r'groupedLocations\"\:\[\{\"localizedName.*?\}\,\"locations', flags=re.DOTALL)
re_geo_attributes = [
	re.compile(r'longitude\"\:(?P<geo_point__longitude__longitude>[^\"]+)\,', flags=re.DOTALL),
	re.compile(r'latitude\"\:(?P<geo_point__latitude__latitude>[^\"]+)\,', flags=re.DOTALL),
	re.compile(r'localizedName\"\:\"(?P<geo_point__geo_point_name__geo_point_name>[^\"]+)\"\,', flags=re.DOTALL),
]

re_location_block = re.compile(r'locations\"\:\[\{.*?\}\]\,', flags=re.DOTALL)
re_location_attributes = [
	re.compile(r'country\"\:\"(?P<location__location_country__country>[^\"]*?)\"', flags=re.DOTALL),
	re.compile(r'geographicArea\"\:\"(?P<location__location_area__area>[^\"]*?)\"', flags=re.DOTALL),
	re.compile(r'city\"\:\"(?P<location__location_city__city>[^\"]*?)\"', flags=re.DOTALL),
	re.compile(r'postalCode\"\:\"(?P<location__location_postal_code__postal_code>[^\"]*?)\"', flags=re.DOTALL),
	re.compile(r'line1\"\:\"(?P<location__location_address_line1__address>[^\"]*?)\"', flags=re.DOTALL),
	re.compile(r'line2\"\:\"(?P<location__location_address_line2__address>[^\"]*?)\"', flags=re.DOTALL),
	re.compile(r'\"(?P<location__location_type__location_type>[^\"]*?)\"\:true', flags=re.DOTALL),
]

re_specialities = re.compile(r'specialities\"\:\[[^\[\]]*?\]\,')
re_specialities_element = re.compile(r'\"(?P<organization__organization_speciality__organization_speciality>[A-z]+[^\"]+[A-z]+)\"', flags=re.DOTALL)

########
re_similary_company_block = re.compile(r'\{\"entityUrn\"\:\"urn\:li\:fs_normalized.*?\}\}', flags=re.DOTALL)
re_similar_company_attribtes = [
	re.compile(r'\"name\"\:\"(?P<similar_organization__organization_name__organization_name>[^\"]+)\"\,', flags=re.DOTALL),
	re.compile(r'li\:company\:(?P<similar_organization__fsd_organization__fsd_company>\d+)\"\,', flags=re.DOTALL),
	re.compile(r'li\:company\:(?P<similar_organization__fsd_organization__fsd_company>\d+)\"\,', flags=re.DOTALL),
	re.compile(r'li\:fs_industry\:(?P<similar_organization__fsd_industry__fsd_industry>\d+)\"', flags=re.DOTALL),
	re.compile(r'\"universalName\"\:\"(?P<similar_organization__organization_id__organization_id>[^\"]+)\",', flags=re.DOTALL),
	re.compile(r'https\://www\.linkedin\.com/(?P<similar_organization__organization_orgnization_type__orgnization_type>[a-z]*?)\/', flags=re.DOTALL),
	re.compile(r'\"url\"\:\"(?P<similar_organization__organization_page_url__url>[^\"]*?linkedin\.com[^\"]*?)\"\,', flags=re.DOTALL),
	re.compile(r'\"start\"\:(?P<similar_organization__organization_size_start_number__number>\d+)\,', flags=re.DOTALL),
	re.compile(r'\"end\"\:(?P<similar_organization__organization_size_end_number__number>\d+)\,', flags=re.DOTALL),
]

re_similary_company_heardquatar_block = re.compile(r'headquarter\"\:\{[^\{\}]*?\}', flags=re.DOTALL)
re_similary_company_heardquatar_attributes = [
	re.compile(r'country\"\:\"(?P<headquarter__headquarter_country__country>[^\"]+)\"\,', flags=re.DOTALL),
	re.compile(r'geographicArea\"\:\"(?P<headquarter__headquarter_geographic_area__geographic_area>[^\"]+)\"\,', flags=re.DOTALL),
	re.compile(r'city\"\:\"(?P<headquarter__headquarter_city__city>[^\"]+)\"\,', flags=re.DOTALL),
	re.compile(r'postalCode\"\:\"(?P<headquarter__headquarter_postal_code__postal_code>[^\"]+)\"\,', flags=re.DOTALL),
	re.compile(r'line1\"\:\"(?P<headquarter__headquarter__address_line1__address>[^\"]+)\"\,', flags=re.DOTALL),
	re.compile(r'line2\"\:\"(?P<headquarter__headquarter__address_line2__address>[^\"]+)\"\,', flags=re.DOTALL),
]

re_similar_company_logo_block =	re.compile(r'\"logo\"\:\{\"image\"\:.*?CompanyLogoImage\"\}\,', flags=re.DOTALL)
re_similar_company_logo_attributes = [
	re.compile(r'rootUrl\"\:\"(?P<photo_url__photo_root_url__photo_root_url>[^\"]*?)\"\,', flags=re.DOTALL),
	re.compile(r'\"width\"\:400\,\"fileIdentifyingUrlPathSegment\"\:\"(?P<photo_url__photo_segmentation_url__photo_segmentation_url>[^\"]*?)\"\,', flags=re.DOTALL),
]

re_similar_company_backgroud_block = re.compile(r'\"backgroundCoverImage\"\:\{\"image\".*?BackgroundImage\"', flags=re.DOTALL)
re_similar_company_backgroud_attributers = [
	re.compile(r'rootUrl\"\:\"(?P<photo_url__photo_root_url__photo_root_url>[^\"]*?)\"\,', flags=re.DOTALL),
	re.compile(r'\"width\"\:10000\,\"fileIdentifyingUrlPathSegment\"\:\"(?P<photo_url__photo_segmentation_url__photo_segmentation_url>[^\"]*?)\"\,', flags=re.DOTALL),
]


def company_page_parsing(page_html,
	page_url = None):
	output = []
	###
	if page_url is not None:
		output.append({'organization__organization_page_url__page_url':page_url})
		for r in re_url_attrbites:
			for m in re.finditer(r, page_url):
				g = m.groupdict()
				output.append(g)	
	###
	for r in re_company_profile:
		for m in re.finditer(r, page_html):
			g = m.groupdict()
			####
			output.append(g)
	###
	for m in re.finditer(re_location_block, page_html):
		b = m.group()
		location_infor = {}
		for r in re_location_attributes:
			for m1 in re.finditer(r,b):
				g = m1.groupdict()
				location_infor.update(g)
		location_text = ' '.join([location_infor[k] for k in location_infor])
		location_infor['location'] = location_text
		output.append(location_infor)
	###
	for m in re.finditer(re_geo_block, page_html):
		b = m.group()
		location_infor = {}
		for r in re_geo_attributes:
			for m1 in re.finditer(r,b):
				g = m1.groupdict()
				location_infor.update(g)
		output.append(location_infor)
	###
	for s in re.finditer(re_specialities, page_html):
		s1 = s.group()
		for r in re.finditer(re_specialities_element,
			s1):
			output.append(r.groupdict())
	###similar company blcok
	for m in re.finditer(re_similary_company_block, page_html):
		b = m.group()
		####find the similary company attribuets
		similar_company_infor = {}
		for r in re_similar_company_attribtes:
			for m1 in re.finditer(r, b):
				similar_company_infor.update(m1.groupdict())
		####find the similary company logo
		for m1 in re.finditer(re_similar_company_logo_block, b):
			logo_block = m1.group()
			similar_company_logo_infor = {}
			for r1 in re_similar_company_logo_attributes:
				for m2 in re.finditer(r1, logo_block):
					similar_company_logo_infor.update(m2.groupdict())
			if 'photo_url__photo_root_url__photo_root_url' in similar_company_logo_infor and 'photo_url__photo_segmentation_url__photo_segmentation_url' in similar_company_logo_infor:
				similar_company_logo_infor['photo_url'] = '%s%s'%(similar_company_logo_infor['photo_url__photo_root_url__photo_root_url'],similar_company_logo_infor['photo_url__photo_segmentation_url__photo_segmentation_url'])
				similar_company_infor['similar_organization__organization_logo_url__photo_url'] = similar_company_logo_infor['photo_url']
			output.append(similar_company_logo_infor)
		####fnid the similary compaby backgroud
		for m5 in re.finditer(re_similar_company_backgroud_block, b):
			backgroud_block = m5.group()
			similar_company_logo_infor = {}
			for r1 in re_similar_company_backgroud_attributers:
				for m2 in re.finditer(r1, backgroud_block):
					similar_company_logo_infor.update(m2.groupdict())
			if 'photo_url__photo_root_url__photo_root_url' in similar_company_logo_infor and 'photo_url__photo_segmentation_url__photo_segmentation_url' in similar_company_logo_infor:
				similar_company_logo_infor['photo_url'] = '%s%s'%(similar_company_logo_infor['photo_url__photo_root_url__photo_root_url'],similar_company_logo_infor['photo_url__photo_segmentation_url__photo_segmentation_url'])
				similar_company_infor['similar_organization__organization_photo_url__photo_url'] = similar_company_logo_infor['photo_url']
			output.append(similar_company_logo_infor)
		###find the similary company location
		for m6 in re.finditer(re_similary_company_heardquatar_block, b):
			logo_block = m6.group()
			similar_company_logo_infor = {}
			for r1 in re_similary_company_heardquatar_attributes:
				for m2 in re.finditer(r1, logo_block):
					similar_company_logo_infor.update(m2.groupdict())
			headquarter_text = ' '.join([similar_company_logo_infor[k] for k in similar_company_logo_infor])
			similar_company_logo_infor['headquarter'] = headquarter_text
			similar_company_infor['similar_organization__organization_headquarter__headquarter'] = similar_company_logo_infor['headquarter']
			output.append(similar_company_logo_infor)
		#####find the similary company id
		if 'similar_organization__organization_id__organization_id' in similar_company_infor:
			similar_company_infor['similar_organization'] = 'ln:%s'%(similar_company_infor['similar_organization__organization_id__organization_id'])
			output.append({'organization__similar_organization__similar_organization':similar_company_infor['similar_organization']})
		###add the similary company to the list
		output.append(similar_company_infor)
	####find the company logo and back ground image
	for a in output:
		if 'organization__organization_id__organization_id' in a:
			company_name = re.escape(a['organization__organization_id__organization_id'])
			######logo
			re_company_logo_block = re.compile(r'\/%s.*?\"logo\"\:\{\"image\"\:.*?\.VectorImage"}'%(company_name))
			try:
				b = re.search(re_company_logo_block, page_html).group()
				company_logo_infor = {}
				for r in re_similar_company_logo_attributes:
					for m in re.finditer(r, b):
						company_logo_infor.update(m.groupdict())
				if 'photo_url__photo_root_url__photo_root_url' in company_logo_infor and 'photo_url__photo_segmentation_url__photo_segmentation_url' in company_logo_infor:
					company_logo_infor['photo_url'] = '%s%s'%(
						company_logo_infor['photo_url__photo_root_url__photo_root_url'],
						company_logo_infor['photo_url__photo_segmentation_url__photo_segmentation_url'])
				output.append(company_logo_infor)
				output.append({'organization__organization_logo_url__photo_url':company_logo_infor['photo_url']})
			except:
				pass
			######background
			re_company_photo_block = re.compile(r'\"universalName\"\:\"%s\"\,.*?backgroundCoverImage\"\:\{\"image\".*?\.BackgroundImage'%(company_name), flags=re.DOTALL)
			for m1 in re.finditer(re_company_photo_block, page_html):
				b = m1.group()
				company_logo_infor = {}
				for r in re_similar_company_backgroud_attributers:
					for m in re.finditer(r, b):
						company_logo_infor.update(m.groupdict())
				if 'photo_url__photo_root_url__photo_root_url' in company_logo_infor and 'photo_url__photo_segmentation_url__photo_segmentation_url' in company_logo_infor:
					company_logo_infor['photo_url'] = '%s%s'%(
						company_logo_infor['photo_url__photo_root_url__photo_root_url'],
						company_logo_infor['photo_url__photo_segmentation_url__photo_segmentation_url'])
					output.append(company_logo_infor)
					output.append({'organization__organization_photo_url__photo_url':company_logo_infor['photo_url']})
	####build the main entity for multivalue and link it to the page main entity####
	for e in output:
		if 'organization__organization_id__organization_id' in e:
			output.append({'organization':'ln:%s'%(e['organization__organization_id__organization_id'])})
		if 'industry__industry_name__industry_name' in e:
			e['industry'] = e['industry__industry_name__industry_name']
		if 'location' in e:
			output.append({'organization__organization_location__location':e['location']})
		if 'geo_point__longitude__longitude' in e and 'geo_point__latitude__latitude' in e:
			geo_point_text = '%s,%s'%(e['geo_point__latitude__latitude'], e['geo_point__longitude__longitude'])
			e['geo_point'] = geo_point_text
			output.append({'organization__geo_location__geo_point':geo_point_text})
	###
	return output

'''
import yan_web_page_download 
page_url = 'https://www.linkedin.com/company/microsoft/about/'
page_url = 'https://www.linkedin.com/company/suzhou-rainbow-environmental-equipment-co-ltd/about/'
page_url = 'https://www.linkedin.com/company/group42ai/about/'
page_url = 'https://www.linkedin.com/school/new-york-university/about/'

page_html = yan_web_page_download.download_page_from_url(
	page_url,
	curl_file = '/Downloads/curl_info.sh')

o = company_page_parsing(page_html,
	page_url)


def parsed_to_photo_url(input):
	output = []
	for e in input:
		for k in e:
			if k.split('__')[-1] in ['photo_url']:
				output.append(e[k])
	output = list(set(output))
	return output


for u in parsed_to_photo_url(o):
	print(u)

'''



re_company_list_attributes = [
	re.compile(r'\<a href\=\"https\:\/\/www\.linkedin\.com\/company\/(?P<organization__organization_id__organization_id>[^\\\/]*?)\?trk\=companies\_directory\"\>(?P<organization__organization_name__organization_name>[^\<\>]*?)\<\/a\>', flags=re.DOTALL),
	]

def company_dictionary_list_page(
	page_html,
	page_url = None,
	):
	output = []
	for r in re_company_list_attributes:
		for m in re.finditer(r, page_html):
			company = {}
			company.update(m.groupdict())
			company['organization__organization_page_url__page_url'] = 'https://www.linkedin.com/company/{}/about/'.format(company['organization__organization_id__organization_id'])
			company['company'] = 'ln:{}'.format(company['organization__organization_id__organization_id'])
			output.append(company)
	return output


''''


output = company_dictionary_list_page(
	page_html,
	page_url = None,
	)

for e in output:
	print(e)
'''

############linkedin_company_parsing.py############