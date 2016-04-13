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
    public class ReportsController : Controller
    {
        private CarrierDataEntities database = new CarrierDataEntities();

        // GET: Reports
        public ActionResult Index()
        {
            IEnumerable reports_data = database.Reports.ToList();
            ViewBag.reports = reports_data;
            return View();
        }

        // GET: Reports/Details/5
        public ActionResult Details(int id)
        {
            System.Data.Entity.DbSet<Report> database_Reports = database.Reports;
            ViewBag.user = database_Reports.Find(id);

            if (ViewBag.user != null)
            {
                return View();
            }
            else
            {
                ViewBag.error = "Cet utilisateur n'existe pas.";
                return View("./Error");
            }
        }

        // GET: Reports/Create
        public ActionResult Create(string id)
        {
            if (id != null)
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

        // POST: Reports/Create
        [HttpPost]
        public ActionResult Create()
        {
            NameValueCollection post_data = Request.Form;


            try
            {
                Report new_report = new Report();
                new_report.User_id = Convert.ToInt16(Session["id"].ToString());
                new_report.Shop_id = Request.Form["otp"];
                new_report.Serie = Request.Form["RapportSeries"];

                if (new_report.save() == true)
                {
                    return RedirectToAction("Index");
                }
                else
                {
                    ViewBag.error = "Une erreur est survenue dans la création du rapport";
                    return View("./Error");
                }
            }
            catch
            {
                ViewBag.error = "Une erreur est survenue dans la connexion à la database";
                return View("./Error");
            }
        }

        // GET: Reports/Edit/5
        public ActionResult Edit(int id)
        {
            return View();
        }

        // POST: Reports/Edit/5
        [HttpPost]
        public ActionResult Edit(int id, FormCollection collection)
        {
            try
            {
                // TODO: Add update logic here

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }

        // GET: Reports/Delete/5
        public ActionResult Delete(int id)
        {
            return View();
        }

        // POST: Reports/Delete/5
        [HttpPost]
        public ActionResult Delete(int id, FormCollection collection)
        {
            try
            {
                // TODO: Add delete logic here

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }
    }
}
