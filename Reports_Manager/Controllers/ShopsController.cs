using Reports_Manager.Models;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Reports_Manager.Controllers
{
    public class ShopsController : Controller
    {
        private CarrierDataEntities database = new CarrierDataEntities();

        // GET: Shops
        public ActionResult Index()
        {
            var database_Shops = database.Shops;
            
            if (database_Shops != null)
            {
                IEnumerable shops_data = database_Shops.ToList();

                ViewBag.shops = shops_data;
                return View();
            }
            else
            {
                return View("./Error");
            }
        }

        // GET: Shops/Details/5
        public ActionResult Details(int id)
        {
            return View();
        }

        
    }
}
