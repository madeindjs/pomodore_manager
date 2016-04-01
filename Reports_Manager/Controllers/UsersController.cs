using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Mvc.Ajax;
using Reports_Manager.Models;
using System.Collections;

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

        // GET: users/details/id
        public ActionResult Details(int id)
        {
            var user_data = database.Users.Find(id) ;
            ViewBag.user = user_data ;
            return View();
        }
    }
}
