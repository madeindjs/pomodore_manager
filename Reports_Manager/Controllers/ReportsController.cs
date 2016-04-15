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
            ViewBag.report = database_Reports.Find(id);

            if (ViewBag.report != null)
            {
                return View();
            }
            else
            {
                ViewBag.error = "Ce rapport n'existe pas.";
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

                new_report.User_id =        Convert.ToInt16(Session["id"].ToString());
                new_report.Shop_otp =       Request.Form["otp"];
                new_report.Serie =          Request.Form["RapportSeries"];

                new_report.Description =    Request.Form["description"];
                new_report.Categoriy_id =   String.IsNullOrEmpty(Request.Form["categoriy_id"]) ? 0 : Convert.ToInt32(Request.Form["categoriy_id"]);
                new_report.Asked_by =       Request.Form["asked_by"];

                new_report.T_spend =        String.IsNullOrEmpty(Request.Form["t_spend"]) ? TimeSpan.Parse("0:0:0") : TimeSpan.Parse( Request.Form["t_spend"] );
                new_report.T_travel =       String.IsNullOrEmpty(Request.Form["t_travel"]) ? TimeSpan.Parse("0:0:0") : TimeSpan.Parse(Request.Form["t_travel"]);
                new_report.T_plus =         String.IsNullOrEmpty(Request.Form["t_plus"]) ? TimeSpan.Parse("0:0:0") : TimeSpan.Parse(Request.Form["t_plus"]);

                new_report.Analysis =       Request.Form["analysis"];
                new_report.Facts =          Request.Form["facts"];
                new_report.Forecast =       Request.Form["forecast"];

                new_report.Notes =          Request.Form["notes"];


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
            catch (Exception e)
            {
                System.Diagnostics.Debug.WriteLine(e.Message);
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
