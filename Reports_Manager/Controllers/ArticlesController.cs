using Reports_Manager.Models;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;


namespace Reports_Manager.Controllers
{
    public class ArticlesController : Controller
    {
        private CarrierDataEntities database = new CarrierDataEntities();

        // GET: Articles/Index
        public ActionResult Index()
        {
            System.Data.Entity.DbSet<Article> database_Articles = database.Articles;

            if (database_Articles != null)//I check if there are data into database
            {
                //I get shoplist from database & I group them by OTP
                List<Reports_Manager.Models.Article> articles_list = database_Articles.ToList();
                ViewBag.articles = articles_list ;
                return View();
            }
            else
            {
                ViewBag.error = "La base de données est vide";
                return View("./Error");
            }
        }

        // GET: Articles/Details/5
        public ActionResult Details(int id)
        {
            return View();
        }

    }
}
