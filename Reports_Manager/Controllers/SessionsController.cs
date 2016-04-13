using Reports_Manager.Models;
using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Reports_Manager.Controllers
{
    public class SessionsController : Controller
    {

        private CarrierDataEntities database = new CarrierDataEntities();

        // GET: Session/Create
        public ActionResult Create()
        {
            if (Request.RequestType == "POST")
            {
                NameValueCollection post_data = Request.Form;
                System.Data.Entity.DbSet<User> database_Users = database.Users;
                string email_input = post_data["email"];
                User user = new User();

                try
                {
                    user = database_Users.First(users => users.Email == email_input);
                }
                catch
                {
                    ViewBag.error = "Cet email n'est pas présent dans la database";
                    return View("./Error");
                }

                if (DecryptPassword(user.Password) == post_data["password"])
                {
                    HttpContext.Session["id"] = user.Id ;
                    return RedirectToAction("Index", "Shops", new { area = "" });
                }
                else 
                {
                    ViewBag.error = "Le mot de passe ne correspond pas";
                    return View("./Error");
                }


            }
            else if (HttpContext.Session["id"] != null)
            {
                ViewBag.error = "Vous êtes déjà connecté sous " + HttpContext.Session["id"];
                return View("./Error");
            }
            else
            {
                return View();
            }
        }




        // GET: Session/Delete/5
        public ActionResult Delete()
        {
            HttpContext.Session.RemoveAll();
            return RedirectToAction("Index", "Shops", new { area = "" });
        }

        private string DecryptPassword(string encryptedPassword)
        {
            //Decrypter le mot de passe    
            byte[] passByteData = Convert.FromBase64String(encryptedPassword);
            string originalPassword = System.Text.Encoding.Unicode.GetString(passByteData);
            return originalPassword;
        }

    }
}
