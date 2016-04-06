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
            System.Data.Entity.DbSet<Shop> database_Shops = database.Shops;

            if (database_Shops != null)//I check if there are data into database
            {
                //I get shoplist from database & I group them by OTP
                List<Reports_Manager.Models.Shop> shops_list = database_Shops.ToList();
                ViewBag.shops_grouped = shops_list.GroupBy(shop => shop.Otp);
                return View();
            }
            else
            {
                ViewBag.error = "La base de données est vide";
                return View("./Error");
            }
        }

        // GET: Shops/Details/5
        public ActionResult Details(string id)
        {
            if(id != null)
            {

                System.Data.Entity.DbSet<Shop> database_Shops = database.Shops;
                ViewBag.shop = database_Shops.First(shop => shop.Otp == id);

                if (ViewBag.shop != null)
                {
                    ViewBag.cabinets = database_Shops.Where(shop => shop.Otp == id);
                    return View();
                }
                else
                {
                    ViewBag.error = "Cet OTP n'est pas dans la base de données...";
                    return View("./Error");
                }
            }
            else
            {
                ViewBag.error = "Erreur lors de la récupration du paramètre GET";
                return View("./Error");
            }

        }
    }
}
