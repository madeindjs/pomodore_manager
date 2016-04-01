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

        // GET: Shops/index
        public ActionResult Index()
        {
            var database_Shops = database.Shops;
            
            if (database_Shops != null)//I check if there are data into database
            {
                //I get shoplist from database & I group them by OTP
                List<Reports_Manager.Models.Shop> shops_list = database_Shops.ToList();
                ViewBag.shops_grouped = shops_list.GroupBy(shop => shop.Otp);
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
