from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import csv
import os


class MainPage(webapp.RequestHandler):
    
    
    #def get(self):
    #    self.response.headers['Content-Type'] = 'text/html'
    #    reader = csv.reader(open('items.csv'))
    #    for row in reader:
    #        if row[0].find('nikah') != -1 or row[1].find('nikah') != -1:
    #            self.response.out.write(str(row[0])+"<br>");
                
    def get(self):
        self.response.out.write("<html><head><title>Cari Kajian</title></head><body>")
        try:
            query = self.request.get('q')
        except (TypeError,ValueError):
            query = "nikah"
            
        self.response.out.write("<center>")
        self.response.out.write("<h1>Cari Kajian</h1>")
        self.response.out.write("<form>")
        self.response.out.write("<input type='text' name='q' value='%s' size='55'></input>" %(query)) 
        self.response.out.write("<input type='submit' value='Cari'></input>")
        self.response.out.write("</form>")
        self.response.out.write("</center>")
        
        if query != '':
            listcsv = os.listdir('csv')
            list_csv_reader = list()
            for csvfile in listcsv:
                reader = csv.reader(open("csv/"+csvfile))
                list_csv_reader.append(reader)
            
            #reader = csv.reader(open('items.csv'))
            result_set = set([])
            for reader in list_csv_reader:
                for row in reader:
                    if row[0].lower().find(query) != -1 or row[1].lower().find(query) != -1 or row[2].lower().find(query) != -1 or row[3].lower().decode('utf-8').find(query) != -1:
                        if(row[2] not in result_set):
                            self.response.out.write(u'<a href="%s">%s</a>' % (row[0],row[1]))
                            self.response.out.write('<br>')
                            result_set.add(row[2])

  
        self.response.out.write("</body></html>")
        


application = webapp.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
