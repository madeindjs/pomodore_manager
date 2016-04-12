using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Mvc.Ajax;
using Reports_Manager.Models;
using System.Collections;
using System.Collections.Specialized;

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
                new_user.Firstname = Request.Form["firstname"]; 
                new_user.Lastname = Request.Form["lastname"];
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
    }
}
