using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Mvc.Ajax;
using Reports_Manager.Models;
using System.Collections;
using System.Collections.Specialized;
using System.Web.Security;

namespace Reports_Manager.Controllers
{
    public class UsersController : Controller
    {
        private CarrierDataEntities database = new CarrierDataEntities() ;

        // GET: users/index
        public ActionResult Index()
        {
            IEnumerable users_data = database.Users.ToList();
            ViewBag.users = users_data;
            return View();
        }


        // GET: users/create & signup
        public ActionResult Create()
        {
            if( Request.RequestType == "POST")
            {
                NameValueCollection post_data = Request.Form;

                User new_user = new User() ;
                new_user.Email = Request.Form["email"]; 
                new_user.Firstname = Request.Form["firstname"];
                new_user.Lastname = Request.Form["lastname"];
                new_user.Password = EncryptPassword(Request.Form["password"]);

                if ( new_user.save() == true )
                {
                    return RedirectToAction("Index");
                }
                else
                {
                    ViewBag.error = "Une erreur est survenue dans la création de vote compte";
                    return View("./Error");
                }
            }
            else
            {
                return View();
            }
        }

        // GET: users/details/id
        public ActionResult Details(int id)
        {
            System.Data.Entity.DbSet<User> database_Users = database.Users;
            ViewBag.user = database_Users.Find(id);

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

        private string EncryptPassword(string textPassword)
        {
            //Crypter le mot de passe          
            byte[] passBytes = System.Text.Encoding.Unicode.GetBytes(textPassword);
            string encryptPass = Convert.ToBase64String(passBytes);
            return encryptPass;
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
