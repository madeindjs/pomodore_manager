using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Reports_Manager.Controllers
{
    public class PagesController : Controller
    {
        // GET: Pages
        public ActionResult Home()
        {
            return View();
        }
    }
}