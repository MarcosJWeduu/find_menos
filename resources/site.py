from flask_restful import Resource
from models.site import SiteModel

class Sites(Resource):
    def get(self):
        return {'sites': [site.json() for site in SiteModel.query.all()]}
    
class Site(Resource):
    def get(self, url):
        site=SiteModel.find_site(url)
        if site:
            return site.json()
        return {'message':'Site not found.'}, 404
    
    def post(self, url):
        if SiteModel.find_site(url):
            return{'message':'An site with this URL already exists'}, 400
        site = SiteModel(url)
        try:
            site.save_site()
        except:
            return{"message":"Error while creating the site."},500
        return site.json()
    
    def delete(self, url):
        site = SiteModel.find_site(url)
        if site:
            site.delete_site()
            return {'message':'Site  deleted'}
        return {'messge': 'Site not found'}, 404
