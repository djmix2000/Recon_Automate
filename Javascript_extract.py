import jsbeautifier
import requests
import re


class JavascriptEndpoints:
    def __init__(self,javascript_url_list:list[str]):
        self.endpoints_list = list[str]
        self.javascript_url_list = javascript_url_list


class JavascriptExtract:
    def single(self,url):
        req = JavascriptParse.fetch_js(url)
        absolute_pattern = r'(["\'])(https?://(?:www\.)?\S+?)\1'
        relative_dirs = re.findall('["\'][\w\.\?\-\_]*/[\w/\_\-\s\?\.=]*["\']*', req)
        absolute_urls = re.findall(absolute_pattern, req)
        absolute_urls = [url[1] for url in absolute_urls]
        all_dirs = relative_dirs + absolute_urls
        return all_dirs


class JavascriptParse:
    @staticmethod
    def fetch(url):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
        req = requests.get(url, headers=headers).text
        req = jsbeautifier.beautify(req)
        return req