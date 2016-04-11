using Reports_Manager.Models;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Reports_Manager.Controllers
{
    public class ShopsController : Controller
    {
        private CarrierDataEntities database = new CarrierDataEntities();
        private const int RESULTS_PER_PAGES = 10 ;

        // GET: Shops/index
        public ActionResult Index(int? page)
        {
            return View();
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


        public ActionResult search()
        {
            System.Data.Entity.DbSet<Shop> database_Shops = database.Shops;

            if (database_Shops != null)//I check if there are data into database
            {
                //I get all POSt data
                //string[] post_data = Request.Form;


                NameValueCollection post_data = Request.Form;
                ViewBag.post_data = post_data;


                string search_magasin = !String.IsNullOrEmpty(post_data["magasin"]) ? post_data["magasin"] : "";
                string search_otp = !String.IsNullOrEmpty(post_data["otp"]) ? post_data["otp"] : "";
                string search_code_postal = !String.IsNullOrEmpty(post_data["code_postal"]) ? post_data["code_postal"] : "";
                string search_ville = !String.IsNullOrEmpty(post_data["ville"]) ? post_data["ville"] : "";


                int pageNumber = int.Parse(post_data["n_page"]);

                ViewBag.shops_grouped = database_Shops
                    .Where( shop =>
                        shop.Date_fact != null &&

                        (//shop's name
                            string.IsNullOrEmpty(search_magasin) ||
                            shop.Magasin.ToUpper().Contains( search_magasin.ToUpper() )
                        )&&


                        (//shop's otp
                            string.IsNullOrEmpty(search_otp) ||
                            shop.Otp.ToUpper().Contains(search_otp.ToUpper())
                        )&&

                        (//shop's zip code
                            string.IsNullOrEmpty(search_code_postal) ||
                            shop.Code_postal.ToUpper().Contains(search_code_postal.ToUpper())
                        )&&

                        (//shop's town
                            string.IsNullOrEmpty(search_ville) ||
                            shop.Ville.ToUpper().Contains(search_ville.ToUpper())
                        )

                    )
                    .GroupBy(shop => shop.Otp)
                    .Take(RESULTS_PER_PAGES * pageNumber);

                return PartialView("_List");
            }
            else
            {
                ViewBag.error = "La base de données est vide";
                return View("./Error");
            }
        }
    }
}
