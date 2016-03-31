using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Reports_Manager.Controllers
{
    public class ShopsController : Controller
    {
        // GET: Shops
        public ActionResult Index()
        {
            return View();
        }

        // GET: Shops/Details/5
        public ActionResult Details(int id)
        {
            return View();
        }

        
    }
}
