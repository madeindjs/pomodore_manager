using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Reports_Manager.Controllers
{
    public class ArticlesController : Controller
    {
        // GET: Articles/Index
        public ActionResult Index()
        {
            return View();
        }

        // GET: Articles/Details/5
        public ActionResult Details(int id)
        {
            return View();
        }

    }
}
